# Binary search to find the first index where a[i] >= target
def lower_bound(a, target):
    left = 0
    right = len(a) - 1
    answer = -1

    while left <= right:
        mid = left + (right - left) // 2

        if a[mid] >= target:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

# search for first index satisfying condition (a[i] >= target)
# if condition is true, save answer and move left
# if condition is false, move right
# returns index of first valid element or -1 if not found

# Setup example
a = [1, 3, 5, 7, 9, 11]
target = 6
print(lower_bound(a, target))  # 3

# 🧠 Mental Intuition:
# Imagine your array as a sequence of booleans:
#   false false false true true true
# You want the index of the first true.
# In this case, the "condition" is a[i] >= target.
# This pattern is called "binary search on condition".
# Works as long as condition becomes true and stays true.
