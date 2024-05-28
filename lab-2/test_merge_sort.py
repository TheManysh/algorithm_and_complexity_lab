import unittest
from merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        input = [5, 4, 3, 2, 1]
        output = merge_sort(input)
        self.assertEqual(output, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
