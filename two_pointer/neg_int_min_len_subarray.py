from collections import deque
import math

def min_len_subarray_with_negatives(a, s):
    n = len(a)
    # Prefix sums P[0]=0, P[pos] = sum(a[:pos])
    P = [0]*(n+1)
    for pos in range(1, n+1):
        P[pos] = P[pos-1] + a[pos-1]

    # Deque of candidate left positions (indices into P), with increasing P-values
    left_candidates = deque()
    best_len = math.inf
    best_window = None  # (left_index_in_a, right_index_in_a) inclusive

    for right in range(n + 1):
        # 1) While we can meet s, shrink from the left
        while left_candidates and P[right] - P[left_candidates[0]] >= s:
            left = left_candidates.popleft()
            cur_len = right - left
            if cur_len < best_len:
                best_len = cur_len
                # subarray is a[left : right] => indices in a are [left, right-1]
                best_window = (left, right - 1)

        # 2) Maintain increasing P-values among left candidates
        while left_candidates and P[right] <= P[left_candidates[-1]]:
            left_candidates.pop()

        # 3) Current right becomes a future left candidate
        left_candidates.append(right)

    return (0 if best_len is math.inf else best_len, best_window)
