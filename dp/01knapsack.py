# 0/1 Knapsack Problem

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for item_index in range(n):
        weight = weights[item_index]
        value = values[item_index]

        # Traverse capacity backwards to avoid overwriting results
        for cap in range(capacity, weight - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - weight] + value)

    return dp[capacity]


# Setup exampleweights = [1, 2, 3]
values = [10, 15, 40]
capacity = 6
print(knapsack(weights, values, capacity))  # 55    

# 2d version

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n)]

    # Fill for the first item
    for w in range(capacity + 1):
        if w >= weights[0]:
            dp[0][w] = values[0]

    for item in range(1, n):
        weight = weights[item]
        value = values[item]
        for w in range(capacity + 1):
            # Don't take this item
            dp[item][w] = dp[item - 1][w]
            # Take this item (if it fits)
            if w >= weight:
                dp[item][w] = max(dp[item][w], dp[item - 1][w - weight] + value)

    return dp[n - 1][capacity]