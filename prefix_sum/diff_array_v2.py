from typing import List
from collections import Counter

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        # diff has size n+1 so diff[r+1] is safe
        diff = [0] * (n + 1)

        # Mark range increments
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1  # r+1 is <= n, safe due to size n+1

        # Build cover array via prefix sum
        cover = [0] * n
        curr = 0
        for i in range(n):
            curr += diff[i]
            cover[i] = curr

        # Check if each nums[i] can be decremented to 0
        for i in range(n):
            if nums[i] > cover[i]:
                return False

        return True
