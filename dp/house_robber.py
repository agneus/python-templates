# House Robber Problem
# Maximize amount robbed from non-adjacent houses
def rob(houses):
        max_if_skipped_last = 0      # Like dp[i-2]
        max_if_skipped_current = 0   # Like dp[i-1]

        for value in houses:
            rob_current = value + max_if_skipped_last
            skip_current = max_if_skipped_current
            best_so_far = max(rob_current, skip_current)

            # Slide the window forward
            max_if_skipped_last = max_if_skipped_current
            max_if_skipped_current = best_so_far

        return max_if_skipped_current