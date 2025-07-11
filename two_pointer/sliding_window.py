# Sliding window: maximum sum of any subarray of size k

def max_sum_subarray(nums, k):
    max_sum = float('-inf')
    current_sum = 0
    left = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        if right - left + 1 == k:
            max_sum = max(max_sum, current_sum)
            current_sum -= nums[left]
            left += 1

    return max_sum

# maintain a fixed-size window of size k
# add new element on right, remove leftmost when size exceeds k
# update max on each complete window

# Setup example
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(nums, k))  # 9
