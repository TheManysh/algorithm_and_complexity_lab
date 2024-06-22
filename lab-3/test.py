import unittest
from knapsack_brute_force import knapsack_brute_force
from fractional_knapsack_brute_force import fractional_knapsack_brute_force
from fractional_knapsack_greedy import fractional_knapsack_greedy
from knapsack_dp import knapsack_dp


class TestKnapsackAlgorithms(unittest.TestCase):

    # Test case for Brute-force Method (0/1 Knapsack)
    def test_knapsack_brute_force(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50
        result = knapsack_brute_force(values, weights, capacity)
        self.assertEqual(result, 220)

    # Test case for Brute-force Method (Fractional Knapsack)
    def test_fractional_knapsack_brute_force(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50
        result = fractional_knapsack_brute_force(values, weights, capacity)
        self.assertEqual(result, 240.0)

    # Test case for Greedy Method (Fractional Knapsack)
    def test_fractional_knapsack_greedy(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50
        result = fractional_knapsack_greedy(values, weights, capacity)
        self.assertEqual(result, 240.0)

    # Test case for Dynamic Programming Method (0/1 Knapsack)
    def test_knapsack_dp(self):
        values = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50
        result = knapsack_dp(values, weights, capacity)
        self.assertEqual(result, 220)


if __name__ == '__main__':
    unittest.main()
