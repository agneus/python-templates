import heapq

def dijkstra(adj, src):
    V = len(adj)
    dist = [float('inf')] * V
    dist[src] = 0

    visited = [False] * V

    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)

        if visited[u]:
            continue
        visited[u] = True

        for v, wt in adj[u]:
            if not visited[v] and dist[v] > dist[u] + wt:
                dist[v] = dist[u] + wt
                heapq.heappush(pq, (dist[v], v))

    return dist
