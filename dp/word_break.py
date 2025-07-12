# word break problem
# Classic DP problem to check if a string can be segmented into words from a dictionary 
def word_break(s, word_dict):
    n = len(s)
    word_set = set(word_dict)
    dp = [False] * (n + 1)
    dp[0] = True # base case: empty string can be segmented

    for end in range(1, n + 1):
        for split in range(end):
            if dp[split] and s[split:end] in word_set:
                dp[end] = True

    return dp[n]


# Setup example
s = "leetcode"
word_dict = ["leet", "code"]
print(word_break(s, word_dict))  # True 

# Memoization version
def word_break_memo(s, word_dict):
    n = len(s)
    word_set = set(word_dict)
    memo = {}

    def helper(start):
        if start == n:
            return True
        if start in memo:
            return memo[start]

        for end in range(start + 1, n + 1):
            if s[start:end] in word_set and helper(end):
                memo[start] = True
                return True

        memo[start] = False
        return False

    return helper(0)