# Cycle detection in a directed graph using DFS

UNVISITED, VISITING, VISITED = 0, 1, 2

def has_cycle(graph):
    n = len(graph)
    status = [UNVISITED] * n
    found_cycle = False

    def dfs(u):
        nonlocal found_cycle
        if status[u] == VISITING:
            found_cycle = True     # back-edge ⇒ cycle
            return
        if status[u] == VISITED:
            return
        status[u] = VISITING       # mark before exploring
        for v in graph[u]:
            dfs(v)
            if found_cycle:
                return
        status[u] = VISITED        # mark after all descendants

    for u in range(n):
        if status[u] == UNVISITED:
            dfs(u)
            if found_cycle:
                return True
    return False

# graph = adjacency list for directed graph
# returns True if a cycle exists, False otherwise

# Setup example (acyclic)
graph1 = [[1], [2], []]
print(has_cycle(graph1))  # False

# Setup example (cycle)
graph2 = [[1], [2], [0]]
print(has_cycle(graph2))  # True
