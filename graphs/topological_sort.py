# Topological sort using DFS and postorder stack
def topo_sort():
    for node in range(n):
        if not visited[node]:
            dfs(node)
    return stack[::-1]

def dfs(node):
    if visited[node]:
        return
    
    visited[node] = True

    for neighbor in graph[node]:
        dfs(neighbor)

    stack.append(node)

# visit unvisited nodes
# recurse on neighbors before pushing to stack
# reverse the stack at the end

# Setup
n = 6  # number of nodes
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]
stack = []

# Example DAG edges
graph[5].extend([2, 0])
graph[4].extend([0, 1])
graph[2].extend([3])
graph[3].extend([1])
