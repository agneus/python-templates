from functools import lru_cache

def lcs_length(a: str, b: str) -> int:
    n, m = len(a), len(b)

    @lru_cache(None)
    def dp(i: int, j: int) -> int:
        # i and j represent prefix lengths a[:i], b[:j]
        if i == 0 or j == 0:
            return 0

        if a[i - 1] == b[j - 1]:
            return 1 + dp(i - 1, j - 1)

        return max(dp(i - 1, j), dp(i, j - 1))

    return dp(n, m)   # ✅ intuitive: LCS of full strings


# iterative
def lcs(a, b):
    n, m = len(a), len(b)
    # dp[i][j] = LCS length of s[:i] and t[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
