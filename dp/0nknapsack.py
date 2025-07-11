# Classical Unbounded Knapsack Problem
# Maximize total value with unlimited supply of each item

def unbounded_knapsack_1d(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for item_index in range(len(weights)):
        weight = weights[item_index]
        value = values[item_index]
        for cap in range(weight, capacity + 1):
            dp[cap] = max(dp[cap], dp[cap - weight] + value)
    return dp[capacity]

def unbounded_knapsack_2d(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n)]
    # base case: only item 0
    first_weight = weights[0]
    first_value = values[0]
    for cap in range(capacity + 1):
        dp[0][cap] = (cap // first_weight) * first_value
    # fill for items 1..n-1
    for item_index in range(1, n):
        weight = weights[item_index]
        value = values[item_index]
        for cap in range(capacity + 1):
            # skip this item
            dp[item_index][cap] = dp[item_index - 1][cap]
            # take this item (unbounded)
            if cap >= weight:
                dp[item_index][cap] = max(
                    dp[item_index][cap],
                    dp[item_index][cap - weight] + value
                )
    return dp[n - 1][capacity]

def unbounded_knapsack_memo(weights, values, capacity):
    memo = {}
    def helper(item_index, remaining_capacity):
        if item_index < 0 or remaining_capacity <= 0:
            return 0
        key = (item_index, remaining_capacity)
        if key in memo:
            return memo[key]
        # skip current item
        best = helper(item_index - 1, remaining_capacity)
        # take current item
        weight = weights[item_index]
        value = values[item_index]
        if remaining_capacity >= weight:
            best = max(best, helper(item_index, remaining_capacity - weight) + value)
        memo[key] = best
        return best

    return helper(len(weights) - 1, capacity)

# Setup example
weights = [2, 3, 4]
values  = [4, 5, 6]
capacity = 5

print(unbounded_knapsack_1d(weights, values, capacity))   # 9
print(unbounded_knapsack_2d(weights, values, capacity))   # 9
print(unbounded_knapsack_memo(weights, values, capacity)) # 9
