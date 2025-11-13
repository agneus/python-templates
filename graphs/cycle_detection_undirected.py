# Cycle detection in an undirected graph using DFS

def has_cycle_undirected(graph):
    n = len(graph)
    visited = [False] * n

    def dfs(u, parent):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                if dfs(v, u):      # go deeper
                    return True
            elif v != parent:
                # saw a neighbor we've already visited
                # and it's NOT the node we came from → loop exists
                return True
        return False

    # graph might be disconnected
    for u in range(n):
        if not visited[u]:
            if dfs(u, -1):
                return True
    return False


# graph = adjacency list for UNDIRECTED graph
# (for every edge u-v, both u lists v and v lists u)
# returns True if a cycle (loop) exists, False otherwise

# Example 1: tree (no cycle)
# 0 - 1 - 2
graph1 = [
    [1],    # 0
    [0, 2], # 1
    [1]     # 2
]
print(has_cycle_undirected(graph1))  # False

# Example 2: simple cycle
# 0 - 1 - 2 - 0
graph2 = [
    [1, 2], # 0
    [0, 2], # 1
    [0, 1]  # 2
]
print(has_cycle_undirected(graph2))  # True
