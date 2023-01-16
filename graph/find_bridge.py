def find_bridges(graph):
    """
    Find all bridges in an undirected graph.
    :param graph: A dictionary representing an undirected graph, where each key is a vertex
    and the value is a set of vertices that are connected to the key vertex.
    :return: A list of tuples, where each tuple represents a bridge in the form (u, v).
    """
    def dfs(v, visited, disc, low, parent, bridges):
        """
        Depth-first search function to find bridges.
        """
        visited[v] = True
        disc[v] = low[v] = time
        time += 1

        for u in graph[v]:
            if not visited[u]:
                parent[u] = v
                dfs(u, visited, disc, low, parent, bridges)
                low[v] = min(low[v], low[u])
                if low[u] > disc[v]:
                    bridges.append((v, u))
            elif u != parent[v]:
                low[v] = min(low[v], disc[u])

    visited = {v: False for v in graph}
    disc = {v: float('inf') for v in graph}
    low = {v: float('inf') for v in graph}
    parent = {v: None for v in graph}
    bridges = []
    time = 0

    for v in graph:
        if not visited[v]:
            dfs(v, visited, disc, low, parent, bridges)

    return bridges
