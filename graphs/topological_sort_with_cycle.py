# Topological Sort with Cycle Detection — refined DFS pattern
# Here's the thing - this is for DAGs with natural edges u -> v.
# If you have edges v -> u, like in course schedule, just return the order as is, not reversed.

UNVISITED = 0
VISITING  = 1
VISITED   = 2

def topo_sort_with_cycle(graph):  # graph is an adjacency list
    n = len(graph)
    status = [UNVISITED] * n
    order = []

    def dfs(node):
        # hit a node that is currently on the stack → cycle
        if status[node] == VISITING:
            return True  # cycle found
        # already fully processed
        if status[node] == VISITED:
            return False

        status[node] = VISITING
        for nei in graph[node]:
            if dfs(nei):
                return True
        status[node] = VISITED
        order.append(node)
        return False

    for u in range(n):
        if status[u] == UNVISITED:
            if dfs(u):
                return None  # cycle detected

    return order[::-1]  # for "u -> v means u before v"

# Setup example (DAG)
graph = [
    [1, 2],  # 0 → 1, 2
    [2],     # 1 → 2
    []       # 2 → 
]
print(topo_sort_with_cycle(graph))  # [0, 1, 2]

# Setup example (cycle)
graph_cycle = [
    [1],
    [2],
    [0]
]
print(topo_sort_with_cycle(graph_cycle))  # None