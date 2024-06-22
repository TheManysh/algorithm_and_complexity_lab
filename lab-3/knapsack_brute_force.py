def knapsack_brute_force(values, weights, capacity):
    n = len(values)
    max_value = 0

    def explore(index, current_weight, current_value):
        nonlocal max_value
        if index == n:
            if current_weight <= capacity:
                max_value = max(max_value, current_value)
            return

        # Exclude current item
        explore(index + 1, current_weight, current_value)

        # Include current item
        if current_weight + weights[index] <= capacity:
            explore(index + 1, current_weight +
                    weights[index], current_value + values[index])

    explore(0, 0, 0)
    return max_value
