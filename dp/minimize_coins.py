# minimize coins to reach target amount

def minimize_coins(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[target] if dp[target] != float('inf') else -1


# setup example
coins = [1, 2, 5]
target = 11
print(minimize_coins(coins, target))  # 3 (11 = 5 + 5 + 1)
# Explanation: 3 coins needed (5, 5, 1)
# If target cannot be reached, returns -1
# Example: coins = [2, 3, 5], target = 7
# Output: 2 (7 = 5 + 2)

# memoization version
def minimize_coins_memo(coins, target):
    memo = {}

    def helper(amount):
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]
        
        min_coins = float('inf')
        for coin in coins:
            min_coins = min(min_coins, helper(amount - coin) + 1)

        memo[amount] = min_coins
        return min_coins
    
    return helper(target) if helper(target) != float('inf') else -1


