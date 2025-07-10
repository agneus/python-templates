# Binary search for target in sorted array
def binary_search(a, target):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if a[mid] == target:
            return mid
        elif a[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# while left <= right
# return mid if found
# shift bounds depending on comparison
# return -1 if not found

a = [1, 3, 5, 7, 9, 11]
target = 7
print(binary_search(a, target))  # 3
