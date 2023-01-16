"""
Initialize an empty list to store the bridges and a variable to keep track of the current time.
For each vertex in the graph, do the following:
a. If the vertex has not been visited, call a depth-first search (DFS) function with the vertex as the starting point.
b. In the DFS function, mark the vertex as visited and set its discovery time to the current time.
c. For each unvisited neighbor of the vertex, call the DFS function with the neighbor as the starting point and set the vertex as the parent of the neighbor.
d. Compare the discovery time and the low-link value of each neighbor and update the low-link value of the vertex accordingly.


--------> e. If the low-link value of a neighbor is greater than the discovery time of the vertex,
 add the edge between the vertex and the neighbor to the list of bridges.
"""
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
