import unittest
from arrays_05_first_recurring_character import first_recurring_character


class MyTestCase(unittest.TestCase):
    def test_correct_number_1(self):
        self.assertEqual(first_recurring_character([2, 5, 1, 2, 3, 5, 1, 2, 4]), 2)

    def test_correct_number_2(self):
        self.assertEqual(first_recurring_character([2, 1, 1, 2, 3, 5, 1, 2, 4]), 1)

    def test_correct_number_3(self):
        self.assertEqual(first_recurring_character([2, 3, 4, 5]), None)


if __name__ == '__main__':
    unittest.main()
