# 3. Count of subarrays with sum <= s

def count_subarrays_with_sum_leq(a, s):
    left = 0
    current_sum = 0
    count = 0

    for right in range(len(a)):
        current_sum += a[right]
        while current_sum > s:
            current_sum -= a[left]
            left += 1
        count += right - left + 1

    return count

# for each right, count how many valid lefts exist
# each valid (left, right) pair is a valid subarray

# Example
# a = [1, 2, 3], s = 3 => returns 4
