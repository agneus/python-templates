import heapq

def dijkstra(adj, src):
    V = len(adj)
    dist = [float('inf')] * V
    dist[src] = 0

    visited = [False] * V
    pq = [(0, src)]  # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)

        if visited[u]:
            continue
        visited[u] = True

        for v, wt in adj[u]:
            if dist[v] > d + wt:
                dist[v] = d + wt
                heapq.heappush(pq, (dist[v], v))

    return dist
