import builtins
import unittest

import re

def_re = '(.*)(def\s+)(.*)(\()(.*)(\)\s*\:)(.*)'
class_re = '(.*)(class\s+)(.*)'
quoted_re = '([\"\'])(?:(?=(\\?))\2.)*?\1'


# extracts left parts
def analyze_clause(cleaned, tgts, res, with_equal_sign=True):
    pos = 0
    l = len(cleaned)
    while pos < l and ((pos + 1 < l and cleaned[pos] == '=' and cleaned[pos + 1] == '=') or cleaned[pos] != '='):
        pos += 1
    if pos < l or not with_equal_sign:
        for var in cleaned[:pos].split(','):
            v = var.strip()
            if v in tgts:
                res.add(v)


def analyze_class_name(cleaned, tgts, res):
    pos = 0
    l = len(cleaned)
    while pos < l and cleaned[pos] != '(' and cleaned[pos] != ':':
        pos += 1
    name = cleaned[:pos].strip()
    if name in tgts:
        res.add(name)


def clean(line):
    """
    removes quoted text
    :param line: line to clean from quoted substrings
    :return:
    """
    pos = 0
    to_remove = []
    found = True
    line = line.replace('"""', '"')
    line = line.replace('\'\'\'', '\'')
    ln = len(line)
    l = 0
    r = 0
    count = 0
    while pos < ln:
        found = False
        while pos < ln and line[pos] != '"':
            pos += 1
        if pos < ln:
            l = pos
            pos += 1
            while pos < ln and line[pos] != '"':
                pos += 1
            if pos < ln:
                r = pos
                found = True
                count += 1
        if found:
            line = line[:l] + line[r + 1:]
        else:
            break
        ln = len(line)
    ln = len(line)
    l = 0
    r = 0
    count = 0
    while pos < ln:
        found = False
        while pos < ln and line[pos] != "'":
            pos += 1
        if pos < ln:
            l = pos
            pos += 1
            while pos < ln and line[pos] != "'":
                pos += 1
            if pos < ln:
                r = pos
                found = True
                count += 1
        if found:
            line = line[:l] + line[r + 1:]
        else:
            break
        ln = len(line)

    return line


def find_variable_assignments(src, tgts):
    lines = src.split('\n')
    result = set()
    for ln in lines:
        line = clean(ln)
        rematch = re.match(class_re, line)
        if rematch:  # class definition
            analyze_class_name(rematch.group(3).strip(), tgts, result)
            continue

        rematch = re.match(def_re, line)
        if rematch:  # function definition
            name = rematch.group(3).strip()
            if name in tgts:
                result.add(name)
            params = rematch.group(5).strip()

            for param in params.split(','):
                analyze_clause(param.strip(), tgts, result, False)

            body = rematch.group(7).strip()
            analyze_clause(body, tgts, result)

        else:  # body line
            analyze_clause(line, tgts, result)
    return result


class TestFindVariableAssignments(unittest.TestCase):
    def test_regular_assignment(self):
        src = """
def fn():
    str = 42
    a, b = 1, 2
    print(str, a, b)
"""
        expected = ["str"]
        targets = dir(builtins)
        self.assertCountEqual(find_variable_assignments(src, targets), expected)

    def test_ignores_edge_cases(self):
        src = """
def fn():
    "str = 42"
    '''next=42'''
    'bin = dir = next = list'
    next == 42
    a, b = str, list
    print(str, a, b)
"""
        expected = []
        targets = dir(builtins)
        self.assertCountEqual(find_variable_assignments(src, targets), expected)

    def test_ignores_values(self):
        src = """
def fn():
    next = 42
    str = next
    a, b = tuple, list
"""
        expected = ["next", "str"]
        targets = dir(builtins)
        self.assertCountEqual(find_variable_assignments(src, targets), expected)

    def test_multiple_assignments(self):
        src = """
def fn(): 
    next,dir,list,dir = 1,2,3,"bin = 4"
str = 45
"""
        expected = ["next", "str", "dir", "list"]
        targets = dir(builtins)
        self.assertCountEqual(find_variable_assignments(src, targets), expected)

    def test_single_parameter(self):
        src = "def reverse(str): return str[::-1]"
        expected = ["str"]
        targets = dir(builtins)
        self.assertCountEqual(find_variable_assignments(src, targets), expected)

    def test_multiple_parameters(self):
        src = """
def list(str, foo, iter): 
    def bin(set): 
        dict = 42 
        foo = zip
        bar = 0
    return str[::-1]
"""
        expected = ["str", "list", "iter", "bin", "set", "dict"]
        targets = dir(builtins)
        self.assertCountEqual(find_variable_assignments(src, targets), expected)

    def test_class_with_nested_fn(self):
        src = """
class str: 
    def __init__(self, list): 
        def next(foo, iter=42, baz=1): bin = 2
"""
        expected = ["str", "list", "next", "iter", "bin"]
        targets = dir(builtins)
        self.assertCountEqual(find_variable_assignments(src, targets), expected)
