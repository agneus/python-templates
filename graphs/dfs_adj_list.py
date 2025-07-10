# Depth-First Search (DFS) on an adjacency list graph
def dfs(node):
    if visited[node]:
        return
    
    visited[node] = True

    for neighbor in graph[node]:
        dfs(neighbor)

# visit node if not visited
# mark before recursing
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
