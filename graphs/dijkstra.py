import heapq

def dijkstra(adj, src):
    """
    adj: adjacency list where adj[u] = list of (v, weight)
    src: starting node
    """

    V = len(adj)
    dist = [float('inf')] * V
    dist[src] = 0

    # Priority queue of (distance, node)
    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)

        # Skip stale distances
        if d > dist[u]:
            continue

        # Explore neighbors
        for v, wt in adj[u]:
            if dist[v] > dist[u] + wt:
                dist[v] = dist[u] + wt
                heapq.heappush(pq, (dist[v], v))

    return dist