from bisect import bisect_left
# Longest Increasing Subsequence (LIS) — classic O(n log n) solution
def find_lis(nums):
    dp = []
    for num in nums:
        pos = bisect_left(dp, num)
        if pos == len(dp):
            dp.append(num)
        else:
            dp[pos] = num
    return len(dp)


# O(n^2) solution to find the length of the longest increasing subsequence
def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# memoization version
def find_lis_memo(nums):
    n = len(nums)
    memo = {}

    def longest_from(current_index, last_taken_index):
        # Base case: no more numbers to consider
        if current_index == n:
            return 0

        # Check cached result
        state = (current_index, last_taken_index)
        if state in memo:
            return memo[state]

        # Option 1: skip the current number
        skip = longest_from(current_index + 1, last_taken_index)

        # Option 2: take the current number (if valid)
        take = 0
        if last_taken_index is None or nums[current_index] > nums[last_taken_index]:
            take = 1 + longest_from(current_index + 1, current_index)

        # Cache and return the better of the two
        memo[state] = max(skip, take)
        return memo[state]

    return longest_from(0, None)
