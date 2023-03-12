import unittest
from arrays_03_trapping_rainwater import amount_of_water


class MyTestCase(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(amount_of_water([]), 0)

    def test_one_element_list(self):
        self.assertEqual(amount_of_water([5]), 0)

    def test_correct_solution_1(self):
        self.assertEqual(amount_of_water([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]), 8)


if __name__ == '__main__':
    unittest.main()




if __name__ == '__main__':
    unittest.main()
