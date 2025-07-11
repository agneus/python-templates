# Difference array: range updates in constant time

def find_prefix_sums(a):
    n = len(a)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + a[i]
    return prefix_sums

def find_differences(arr):
    n = len(arr)
    diff = [0] * (n - 1)
    for i in range(n - 1):
        diff[i] = arr[i + 1] = arr[i]
    return diff

def precalc(b):
    b = [0] + b
    return find_differences(b)

def postcalc(a):
    final = find_prefix_sums(a)
    return final[1:]  # remove the extra leading 0

# to update [l, r): diff[l] += d, diff[r] -= d
# then rebuild final array using prefix sum

# Setup example
b = [5, 5, 5, 5, 5]
diff = precalc(b)

updates = [
    (1, 4, 2),  # add 2 to b[1], b[2], b[3]
    (0, 2, -1)  # subtract 1 from b[0], b[1]
]

for l, r, d in updates:
    diff[l] += d
    if r < len(b):
        diff[r] -= d

final_b = postcalc(diff)
print(final_b)  # [4, 6, 7, 7, 5]
