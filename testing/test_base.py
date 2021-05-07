import unittest


def process_text(text):
    if text is None:
        return None
    return text.replace('a', 'b')


class TestFindVariableAssignments(unittest.TestCase):

    def test_regular_text(self):
        sample_1 = 'eva'
        self.assertEquals(process_text(sample_1), 'evb')

    def test_null_safe(self):
        sample_1 = None
        self.assertIsNone(process_text(sample_1))
