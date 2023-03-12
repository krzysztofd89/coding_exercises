import unittest
from arrays_02_container_with_most_water import largest_area


class MyTestCase(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(largest_area([]), 0)

    def test_one_element_list(self):
        self.assertEqual(largest_area([5]), 0)

    def test_correct_solution_1(self):
        self.assertEqual(largest_area([7, 1, 2, 3, 9]), 28)

    def test_correct_solution_2(self):
        self.assertEqual(largest_area([6, 9, 3, 4, 5, 8]), 32)


if __name__ == '__main__':
    unittest.main()

