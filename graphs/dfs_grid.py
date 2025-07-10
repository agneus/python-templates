# Depth-First Search (DFS) implementation for a grid
def dfs(row, col):
    if not is_valid(row, col):
        return
    
    visited[row][col] = True

    for dr, dc in directions:
        dfs(row + dr, col + dc)

# Base Case at the Top: If it’s invalid (out of bounds, wall, visited), bail early.
# mark visited before recursing

# Default helpers
def is_valid(row, col):
    return (0 <= row < rows and 
            0 <= col < cols and 
            not visited[row][col] and 
            grid[row][col] == 1)

# setup
rows, cols = 5, 5 
grid = [[0 for _ in range(cols)] for _ in range(rows)]
visited = [[False for _ in range(cols)] for _ in range(rows)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 