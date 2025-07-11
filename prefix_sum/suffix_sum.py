# Suffix Sum Computation
def compute_suffix_sums(a):
    n = len(a)
    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + a[i]
    return suffix

# usage:
# suffix[i] = sum of elements from a[i] to a[n-1]
# Example
a = [2, 4, 1, 3, 5]
suffix = compute_suffix_sums(a)
# [l, r) is inclusive of l and exclusive of r]
l = 1  # inclusive  
r = 4  # exclusive
print(suffix[l] - suffix[r])  # sum of a[1..3]
# Output: 4 + 1 + 3 = 8
# suffix[1] = 4 + 1 + 3 + 5 = 13
# suffix[4] = 5 


# example usage# Product of array except self using prefix/suffix products

def product_except_self(nums):
    n = len(nums)
    prefix = [1] * (n + 1)  # prefix[i] = product of nums[0:i]
    suffix = [1] * (n + 1)  # suffix[i] = product of nums[i:n]

    for i in range(n):
        prefix[i + 1] = prefix[i] * nums[i]

    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i]

    result = [prefix[i] * suffix[i + 1] for i in range(n)]
    return result

# prefix[i+1] = product of elements before i+1
# suffix[i+1] = product of elements after i
# result[i] = prefix[i] * suffix[i+1]

# Setup example
a = [1, 2, 3, 4]
print(product_except_self(a))  # [24, 12, 8, 6]
