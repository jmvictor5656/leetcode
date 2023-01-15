"""
The Johnson algorithm is an efficient algorithm to find the shortest paths between
 all pairs of vertices in a sparse, edge-weighted directed or undirected graph.
 
It is a combination of the Bellman-Ford and Dijkstra algorithms, and has a running time
 of O(V^2 log V + VE) which is faster than running Dijkstra's algorithm for each vertex.
"""

import heapq

def johnson(graph):
    n = len(graph)

    # Bellman-Ford to find the shortest paths from a single source
    def bellman_ford(s):
        dist = [float('inf')] * n
        dist[s] = 0
        for _ in range(n - 1):
            for u in range(n):
                for v, w in graph[u]:
                    dist[v] = min(dist[v], dist[u] + w)
        return dist

    # Dijkstra to find the shortest paths from a single source
    def dijkstra(s, h, dist):
        heap = [(0, s)]
        while heap:
            d, u = heapq.heappop(heap)
            if d != dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))

    # reweight the edges
    h = bellman_ford(0)
    for u in range(n):
        for v, w in graph[u]:
            w += h[u] - h[v]
            graph[u][v] = w

    # find the shortest paths
    dist = [[float('inf')] * n for _ in range(n)]
    for s in range(n):
        dijkstra(s, h, dist[s])

    # un-reweight the paths
    for s in range(n):
        for t in range(n):
            dist[s][t] += h[t] - h[s]

    return dist

"""
In this implementation,
the input graph is represented as an adjacency list,
where the keys are the vertices and the values are lists of tuples representing the edges and their weights.
The function returns a 2D list dist[i][j] representing the shortest distance between vertex i and vertex j.

The Johnson algorithm starts by reweighting the edges of the graph by applying the Bellman-Ford algorithm 
to find the shortest paths from a single source, then it uses Dijkstra's algorithm to find the shortest paths
 between all pairs of vertices in the reweighted graph. Finally, it un-reweights the paths to get the final shortest paths.
"""