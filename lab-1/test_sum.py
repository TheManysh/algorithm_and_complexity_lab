import unittest
from sum import sum


class TestSum(unittest.TestCase):

    def test_sum(self):
        input = [1, 2, 3]
        output = sum(input)
        self.assertEqual(output, 6)


if __name__ == '__main__':
    unittest.main()
