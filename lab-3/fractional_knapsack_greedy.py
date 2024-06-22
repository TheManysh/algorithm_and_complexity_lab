def fractional_knapsack_greedy(values, weights, capacity):
    n = len(values)
    item_ratios = [(values[i] / weights[i], weights[i], values[i])
                   for i in range(n)]
    item_ratios.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    for ratio, weight, value in item_ratios:
        if capacity >= weight:
            capacity -= weight
            total_value += value
        else:
            total_value += ratio * capacity
            break
    return total_value
