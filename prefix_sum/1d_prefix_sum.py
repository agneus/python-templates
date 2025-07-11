# Prefix sum array for fast range queries
def compute_prefix_sum(a):
    n = len(a)
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] = p[i] + a[i]
    return p

# sum of elements in range [l, r) is p[r] - p[l]
# prefix[0] = 0, prefix[i] = sum of a[0..i-1]

# Setup example
a = [2, 4, 1, 3, 5]
prefix = compute_prefix_sum(a)


# [l, r) is inclusive of l and exclusive of r]
l = 1  # inclusive
r = 4  # exclusive
print(prefix[r] - prefix[l])  # sum of a[1..3] => 4 + 1 + 3 = 8