from collections import deque

# Breadth-First Search (BFS) on an adjacency list graph
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# enqueue if not visited
# mark as visited before enqueue
# use adjacency list for neighbors

# Setup
n = 6  # number of nodes
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]

# Example edges
graph[0].extend([1, 2])
graph[1].extend([0, 3])
graph[2].extend([0, 4])
graph[3].extend([1])
graph[4].extend([2, 5])
graph[5].extend([4])
