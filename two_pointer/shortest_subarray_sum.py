# Minimum length subarray with sum >= s

def min_length_subarray(a, s):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(a)):
        current_sum += a[right]
        while current_sum - a[left] >= s:
            current_sum -= a[left]
            left += 1
        if current_sum >= s:
            min_len = min(min_len, right - left + 1)

    return min_len if min_len != float('inf') else 0

# two pointers: tighten left while sum >= s
# track min length of valid window

# Example
# a = [2, 3, 1, 2, 4, 3], s = 7 => returns 2
