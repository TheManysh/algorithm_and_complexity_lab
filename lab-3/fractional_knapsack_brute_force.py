def fractional_knapsack_brute_force(values, weights, capacity):
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

        # Include fractional part of current item
        if current_weight + weights[index] <= capacity:
            explore(index + 1, current_weight +
                    weights[index], current_value + values[index])
        else:
            remaining_capacity = capacity - current_weight
            fractional_value = (
                values[index] / weights[index]) * remaining_capacity
            explore(index + 1, capacity, current_value + fractional_value)

    explore(0, 0, 0)
    return max_value
