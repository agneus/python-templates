# Longest Palindromic Subsequence (LPS) — classic 2D DP
# This is a variation of the Longest Common Subsequence (LCS) problem apparently
def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # base case: every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # fill dp table bottom-up
    for length in range(2, n + 1):        # substring lengths
        for left in range(n - length + 1):
            right = left + length - 1
            if s[left] == s[right]:
                if length == 2:
                    dp[left][right] = 2
                else:
                    dp[left][right] = dp[left + 1][right - 1] + 2
            else:
                dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])

    return dp[0][n - 1]

# Setup example
s = "bbbab"
print(longest_palindromic_subsequence(s))  # 4 ("bbbb")



# Memoization version
def longest_palindromic_subsequence_memo(s):
    n = len(s)
    memo = {}

    def helper(left, right):
        if left > right:
            return 0
        if left == right:
            return 1
        if (left, right) in memo:
            return memo[(left, right)]

        if s[left] == s[right]:
            memo[(left, right)] = 2 + helper(left + 1, right - 1)
        else:
            memo[(left, right)] = max(helper(left + 1, right), helper(left, right - 1))

        return memo[(left, right)]

    return helper(0, n - 1)