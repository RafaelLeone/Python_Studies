import unittest
from main import concatenate_lists, order_list, find_median

class TestFunctions(unittest.TestCase):
    def test_concatenate_lists(self):
        result = concatenate_lists([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_order_list(self):
        result = order_list([3, 1, 2, 5, 4])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_find_median_odd(self):
        result = find_median([1, 2, 3, 4, 5])
        self.assertEqual(result, 3)

    def test_find_median_even(self):
        result = find_median([1, 2, 3, 4])
        self.assertEqual(result, 2.5)

if __name__ == '__main__':
    unittest.main()
