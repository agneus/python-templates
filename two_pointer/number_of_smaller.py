# Count, for each b in B, how many elements in A are strictly less than b
def count_smaller(A, B):
    n, m = len(A), len(B)
    i = 0
    result = []

    for b in B:
        while i < n and A[i] < b:
            i += 1
        result.append(i)

    return result

# two pointers: i traverses A as b increases
# since both sorted, no need to reset i for each b
# result[j] = count of A elems < B[j]

# Setup & example
A = [1, 2, 2, 4, 5]
B = [0, 2, 3, 6]
print(count_smaller(A, B))  # [0, 1, 3, 5]
