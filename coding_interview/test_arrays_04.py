import unittest
from arrays_04_merge_sorted_arrays import merge_sorted_arrays


class MyTestCase(unittest.TestCase):
    def test_properly_sorted(self):
        self.assertEqual(merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]), [0, 3, 4, 4, 6, 30, 31])


if __name__ == '__main__':
    unittest.main()
