# 2D prefix sums for fast submatrix queries (right-exclusive bounds)

def compute_prefix_sums_2d(grid):
    rows = len(grid)
    cols = len(grid[0])
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

    for r in range(rows):
        for c in range(cols):
            prefix[r + 1][c + 1] = (
                prefix[r][c + 1] +
                prefix[r + 1][c] -
                prefix[r][c] +
                grid[r][c]
            )

    return prefix

# To query the sum of a submatrix with:
# - top-left corner (top, left)
# - bottom-right corner (bottom, right)
# with right-exclusive bounds: rows [top:bottom), cols [left:right)
#
# Use:
#   prefix[bottom][right]
# - prefix[top][right]
# - prefix[bottom][left]
# + prefix[top][left]

# Setup example
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
prefix = compute_prefix_sums_2d(grid)

# Query sum of submatrix grid[1:3][1:3] → elements [5,6],[8,9]
top, left = 1, 1
bottom, right = 3, 3
print(prefix[bottom][right] - prefix[top][right] - prefix[bottom][left] + prefix[top][left])  # 28
