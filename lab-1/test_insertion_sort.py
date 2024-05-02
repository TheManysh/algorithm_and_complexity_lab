import unittest
from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test_insertion(self):
        input = [5, 4, 3, 2, 1]
        output = insertion_sort(input)
        self.assertEqual(output, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
