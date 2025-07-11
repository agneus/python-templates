# Sliding window skeleton for variable-size window problems

left = 0
for right in range(len(a)):
    add(a[right])

    while not good():
        remove(a[left])
        left += 1

    # process window [left, right] if needed

# right expands window, left contracts until constraint is satisfied
# add/remove manage state (like sum, count, freq, etc.)
# 'good()' checks if current window satisfies the problem constraint

# This is the gold-standard pattern for problems like:
# - longest substring with k distinct characters
# - shortest subarray with at least k occurrences
# - max freq window with allowed replacements

# Just define:
# - add(x): update window state to include x
# - remove(x): remove x from the left end of window
# - good(): return True if window is valid
