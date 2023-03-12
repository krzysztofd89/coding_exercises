import unittest
from arrays_01_two_sums import find_two_sum


class MyTestCase(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_two_sum([], 5), None)

    def test_one_element_list(self):
        self.assertEqual(find_two_sum([5], 5), None)

    def test_correct_solution(self):
        self.assertEqual(find_two_sum([1, 2, 3, 5, 7, 9], 11), [1, 5])

    def test_no_solution(self):
        self.assertEqual(find_two_sum([1, 2, 3, 5, 7, 5], 11), None)

    def test_same_value(self):
        self.assertEqual(find_two_sum([3, 3], 6), [0, 1])


if __name__ == '__main__':
    unittest.main()
