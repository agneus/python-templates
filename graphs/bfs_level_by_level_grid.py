from collections import deque

rows, cols = 5, 5
grid = [[0 for _ in range(cols)] for _ in range(rows)]
visited = [[False for _ in range(cols)] for _ in range(rows)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Breadth-First Search (BFS) that processes the grid level-by-level
def bfs(start_row, start_col):
    queue = deque()
    queue.append((start_row, start_col))
    visited[start_row][start_col] = True
    steps = 0

    while queue:
        for _ in range(len(queue)):  # process one level
            row, col = queue.popleft()

            if is_goal(row, col):
                return steps

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if is_valid(new_row, new_col):
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))

        steps += 1

    return -1  # goal not reachable

# track levels using a loop over the current queue length
# mark as visited before enqueuing
# return early when goal is found

# Default helpers
def is_valid(row, col):
    return (0 <= row < rows and 
            0 <= col < cols and 
            not visited[row][col] and 
            grid[row][col] == 1)

def is_goal(row, col):
    return (row, col) == (target_row, target_col)

# set goal cell
target_row, target_col = 4, 4
