# Longest segment with at most k distinct numbers

def longest_k_distinct_segment(a, k, m):
    cnt = [0] * m  # frequency array for values 0 to m-1
    num = 0        # number of distinct elements
    left = 0
    best = [0, -1]  # store [left, right] of longest valid segment

    for right in range(len(a)):
        cnt[a[right]] += 1
        if cnt[a[right]] == 1:
            num += 1

        while num > k:
            cnt[a[left]] -= 1
            if cnt[a[left]] == 0:
                num -= 1
            left += 1

        if right - left > best[1] - best[0]:
            best = [left, right]

    return best

# maintain window [left, right] such that num <= k
# cnt[x] = frequency of x in current window
# num = distinct elements in window
# best = longest such window
