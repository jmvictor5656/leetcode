"""
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

"""
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        d = [[float('inf') for _ in range(n)] for _ in range(n)]

        for u, v, w in edges:
            d[u][v] = w
            d[v][u] = w

        for i in range(n):
            d[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        
        minimum = float('inf')
        result = 0

        for i in range(n):
            count = 0
            for j in range(n):
                if d[i][j] <= distanceThreshold:
                    count += 1
            if count <= minimum:
                minimum = count
                result = i
        return result