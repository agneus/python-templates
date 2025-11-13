# Directed Cycle detection in a directed graph using DFS

UNVISITED, VISITING, VISITED = 0, 1, 2

def has_cycle(graph):
    n = len(graph)
    status = [UNVISITED] * n

    def dfs(u):
        # hit a node already on the current path → found a loop
        if status[u] == VISITING:
            return True
        # already checked this node fully before
        if status[u] == VISITED:
            return False

        status[u] = VISITING  # we're now walking through u
        for v in graph[u]:
            if dfs(v):        # if any path from v loops, bubble it up
                return True
        status[u] = VISITED   # done exploring from u
        return False

    # graph might be disconnected, so start from every unvisited node
    for u in range(n):
        if status[u] == UNVISITED:
            if dfs(u):
                return True
    return False


# graph = adjacency list for directed graph
# returns True if a cycle (loop) exists, False otherwise

# Setup example (acyclic)
# 0 -> 1 -> 2
graph1 = [[1], [2], []]
print(has_cycle(graph1))  # False

# Setup example (simple cycle)
# 0 -> 1 -> 2 -> 0
graph2 = [[1], [2], [0]]
print(has_cycle(graph2))  # True

# Setup example (disconnected, one part has a cycle)
# 0 -> 1 -> 2   and   3 -> 4 -> 5 -> 3
graph3 = [[1], [2], [], [4], [5], [3]]
print(has_cycle(graph3))  # True
