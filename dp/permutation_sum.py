# Permutation Sum Problem
# Order matters, coins can be reused
def permutation_sum(coins, target):
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: one way to make sum 0

    for amount in range(1, target + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] += dp[amount - coin]

    return dp[target]

# dp[amount] = number of ways to build amount using ordered coin sequences
# outer loop = build up all possible amounts
# inner loop = try each coin at every amount

# Setup example
coins = [2, 3, 5]
target = 9
print(permutation_sum(coins, target))  # 8

# Memoization version
def permutation_sum_memo(coins, target):
    memo = {}

    def helper(amount):
        if amount < 0:
            return 0
        if amount == 0:
            return 1
        if amount in memo:
            return memo[amount]
        
        total_ways = 0
        for coin in coins:
            total_ways += helper(amount - coin)

        memo[amount] = total_ways
        return total_ways

    return helper(target)