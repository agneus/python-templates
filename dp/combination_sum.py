# Variant Unbounded Knapsack Problem
# Count combinations of coins that sum to target
# Order does NOT matter, coins can be reused

def combination_sum(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1  # one way to make amount 0

    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] += dp[amount - coin]

    return dp[target]

# dp[amount] = number of ways to build amount using combinations of coins
# outer loop = coin type (prevents permutations)
# inner loop = build up all reachable amounts using that coin

# Setup example
coins = [2, 3, 5]
target = 9
print(combination_sum(coins, target))  # 5

# 2D version
def combination_sum_2d(coins, target):
    n = len(coins)
    # dp[i][amount] = # of ways to make 'amount' using coins[0..i]
    dp = [[0] * (target + 1) for _ in range(n)]

    # Base case: using only coins[0], you can build multiples of coins[0]
    for amount in range(target + 1):
        dp[0][amount] = 1 if amount % coins[0] == 0 else 0

    # Fill DP for coins 1..n-1
    for i in range(1, n):
        coin = coins[i]
        for amount in range(target + 1):
            # 1) don't take coin i → inherit ways from previous row
            dp[i][amount] = dp[i - 1][amount]
            # 2) take coin i (unbounded) → stay in row i
            if amount >= coin:
                dp[i][amount] += dp[i][amount - coin]

    return dp[n - 1][target]

# memoization version
def combination_sum_memo(coins, target):
    n = len(coins)
    memo = {}

    def helper(last, amount):
        if amount < 0:
            return 0
        if amount == 0:
            return 1
        if last < 0:
            return 0
        
        key = (last, amount)
        if key in memo:
            return memo[key]
        
        # dont take coin 
        not_take = helper(last - 1, amount)
        # take coin, stay at same last coin
        take = helper(last, amount - coins[last])

        memo[key] = not_take + take
        return memo[key]
    
    return helper(n - 1, target)

