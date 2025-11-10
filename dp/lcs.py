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
