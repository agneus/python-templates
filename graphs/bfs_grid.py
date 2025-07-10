from collections import deque

# Breadth-First Search (BFS) implementation for a grid
def bfs(start_row, start_col):
    queue = deque()
    queue.append((start_row, start_col))
    visited[start_row][start_col] = True
    distance[start_row][start_col] = 0

    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if is_valid(new_row, new_col):
                visited[new_row][new_col] = True
                distance[new_row][new_col] = distance[row][col] + 1
                queue.append((new_row, new_col))

# check validity and mark as visited before adding to the queue
# only add to the queue if valid
# do not recheck when popping from the queue

# Default helpers
def is_valid(row, col):
    return (0 <= row < rows and 
            0 <= col < cols and 
            not visited[row][col] and 
            grid[row][col] == 1)

# Setup
rows, cols = 5, 5
grid = [[0 for _ in range(cols)] for _ in range(rows)]
visited = [[False for _ in range(cols)] for _ in range(rows)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
distance = [[float('inf') for _ in range(cols)] for _ in range(rows)]