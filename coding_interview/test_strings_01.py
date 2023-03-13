import unittest
from strings_01_typed_out_strings import compare_strings


class MyTestCase(unittest.TestCase):
    def test_equal_strings_1(self):
        self.assertEqual(compare_strings("ab#z", "az#z"), True)

    def test_equal_empty_strings(self):
        self.assertEqual(compare_strings("x#y#z#", "a#"), True)

    def test_many_hashes(self):
        self.assertEqual(compare_strings("a###b", "b"), True)

    def test_not_equal_strings(self):
        self.assertEqual(compare_strings("abc#d", "acc#c"), False)

    def test_uppercase(self):
        self.assertEqual(compare_strings("Ab#z", "ab#z"), False)


if __name__ == '__main__':
    unittest.main()
