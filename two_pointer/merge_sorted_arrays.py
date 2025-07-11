# Merge two sorted arrays into a single sorted array

def merge_sorted_arrays(a, b):
    i = 0
    j = 0
    merged = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    while i < len(a):
        merged.append(a[i])
        i += 1

    while j < len(b):
        merged.append(b[j])
        j += 1

    return merged

# two pointers start at beginning of each array
# compare current elements, append smaller one
# drain remaining elements after one array is exhausted

# Setup example
a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
print(merge_sorted_arrays(a, b))  # [1, 2, 3, 4, 5, 6, 7, 8]
