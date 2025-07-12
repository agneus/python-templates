# Topological Sort with Cycle Detection — refined DFS pattern

UNVISITED = 0
VISITING  = 1
VISITED   = 2

def topo_sort_with_cycle(graph):
    n = len(graph)
    status = [UNVISITED] * n
    order = []
    has_cycle = False

    def dfs(node):
        nonlocal has_cycle
        # 1) cycle check
        if status[node] == VISITING:
            has_cycle = True
            return
        # 2) already done
        if status[node] == VISITED:
            return

        status[node] = VISITING  # mark before exploring
        for nei in graph[node]:
            dfs(nei)
            if has_cycle:
                return
        status[node] = VISITED
        order.append(node)

    for u in range(n):
        dfs(u)
        if has_cycle:
            return None  # cycle detected

    return order[::-1]  # reverse post-order = topo order

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
