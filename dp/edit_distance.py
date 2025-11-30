def edit_distance(a, b):
    n = len(a)
    m = len(b)

    # dp[i][j] = minimum edits to turn a[:i] into b[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # base cases
    for i in range(n + 1):
        dp[i][0] = i   # delete all characters
    for j in range(m + 1):
        dp[0][j] = j   # insert all characters

    # fill table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]      # no operation
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # delete
                    dp[i][j - 1],    # insert
                    dp[i - 1][j - 1] # replace
                )

    return dp[n][m]


# Example usage
s = input().strip()
t = input().strip()
print(edit_distance(s, t))

#memo

    @lru_cache(None)
    def dist(i, j):
        # i chars used from a, j chars used from b
        if i == n:        # a is finished → must insert rest of b
            return m - j
        if j == m:        # b is finished → must delete rest of a
            return n - i

        if a[i] == b[j]:
            return dist(i + 1, j + 1)

        # replace a[i] with b[j], delete a[i], insert b[j]
        return 1 + min(
            dist(i + 1, j + 1),  # replace
            dist(i + 1, j),      # delete from a
            dist(i, j + 1),      # insert into a
        )

