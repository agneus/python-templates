# Count Palindromic Substrings — classic 2D DP
# This counts all palindromic substrings in a given string

def count_palindromic_substrings(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0

    for length in range(1, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            if s[left] == s[right]:
                if length <= 2 or dp[left + 1][right - 1]:
                    dp[left][right] = True
                    count += 1

    return count


# memoization version 
# Count palindromic substrings with memoized palindrome check

def count_palindromic_substrings_memo(s):
    n = len(s)
    memo = {}

    def is_pal(left, right):
        if left >= right:
            return True
        key = (left, right)
        if key in memo:
            return memo[key]
        memo[key] = (s[left] == s[right]) and is_pal(left + 1, right - 1)
        return memo[key]

    count = 0
    for left in range(n):
        for right in range(left, n):
            if is_pal(left, right):
                count += 1

    return count

# Setup example
s = "aaa"
print(count_palindromic_substrings_memo(s))  # 6
