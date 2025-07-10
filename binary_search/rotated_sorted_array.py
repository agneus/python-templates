# Search for a target in a rotated sorted array
# Uses two binary searches:
#   1. Find rotation pivot (smallest element)
#   2. Binary search in the correct sorted half

def search(nums, target):
    # Phase 1: Find pivot index (minimum element)
    left = 0
    right = len(nums) - 1
    pivot = 0

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] <= nums[right]:
            pivot = mid
            right = mid - 1
        else:
            left = mid + 1

    # Phase 2: Binary search in the correct half
    if nums[pivot] <= target <= nums[-1]:
        left = pivot
        right = len(nums) - 1
    else:
        left = 0
        right = pivot - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Phase 1 finds index of rotation using binary search (pivot = first element <= last)
# Phase 2 does normal binary search in the sorted subarray that may contain target
# Total complexity: O(log n)
