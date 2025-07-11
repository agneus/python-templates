# Longest subarray with sum <= s

def max_length_subarray(a, s):
    left = 0
    current_sum = 0
    max_len = 0

    for right in range(len(a)):
        current_sum += a[right]
        while current_sum > s:
            current_sum -= a[left]
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len

# two pointers: fixed right, adjust left until sum <= s
# maintain max length of valid subarray

# Example
# a = [1, 2, 1, 0, 1, 1, 0], s = 4 => returns 6