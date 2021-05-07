import sys


def strings_manipulation():
    str1 = 'part1'
    #          \3=='t - excluded
    str2 = 'part2'
    #          \3=='t - included
    str_res = str1[:3] + '|' + str2[3:]
    print(str_res)

    # one-line reverse
    str_rev = str_res[::-1]
    print(str_rev)


def datatype_analysis():
    numeric_pure = '123'
    numeric_signed = '+12'
    numeric_signed_wrong = '+-12'
    alphanumeric_pure = '123abc'
    just_math_op = '+'

    print(f'{numeric_pure} isnumeric ? {numeric_pure.isnumeric()}')
    print(f'{numeric_signed} isnumeric ? {numeric_pure.isnumeric()}')
    print(f'{numeric_signed_wrong} isnumeric ? {numeric_pure.isnumeric()}')
    print(f'{alphanumeric_pure} isnumeric ? {alphanumeric_pure.isnumeric()}')
    print(f'{just_math_op} isnumeric ? {just_math_op.isnumeric()}')


def datatype_conversions():
    int_val_of_true = int(True)
    int_val_of_false = int(False)
    print(f'intValOfTrue={int_val_of_true}')
    print(f'intValOfFalse={int_val_of_false}')
    print(f'bool(1)={bool(1)}')
    print(f'bool(3)={bool(3)}')
    print(f'bool(-3)={bool(-3)}')
    print(f'False + 1={False + 1}')
    char_a = 'a'
    print(f'unicode value of a is {ord(char_a)}')
    char_a = chr(ord(char_a))
    print(f'unicode value of 97 is {char_a}')


def datatype_ranges():
    print(f'{sys.float_info}')
    print(f'{sys.int_info}')

    float_val = 0.3 - 0.1 * 3
    print(f'supposed to be 0 : {float_val}')

    print(f'max_float :{sys.float_info.max}')
    print(f'max_int :{2 ** 32}')


def tuples():
    # one line operation is executed using ephemeral temporary variables
    # note: this is implicit tuple (one can assign individual elements, in real tuple this is impossible)
    a, b = 1, 0
    b, a = a + 1, b
    a += 3

    print(f'a = {a}')
    print(f'b = {b}')

    # build tuple from parts of idiom tuple expression
    tuple_4 = (a, a, b)
    print(f'(a, a, b) = {tuple_4}')

    # real tuple
    # Note: tuple is Immutable objects!
    tuple_1 = (0, 1, 2)
    tuple_2 = (3, -1, 1)

    tuple_3 = tuple_1 + tuple_2  # the only structural operation on tuples - concatenation
    print(f'tuple_3 = {tuple_3}')

    complex_1 = 4 + 3j
    complex_2 = 4 - 5j

    complex_sum = complex_1 + complex_2
    print(f'4 + 3j + 4 - 5j = {complex_sum}')


def main():
    strings_manipulation()
    datatype_analysis()
    datatype_conversions()
    datatype_ranges()
    tuples()


if __name__ == '__main__':
    main()
