"""
LEETCODE
743. Network Delay Time

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortest_path = {i: float('inf') if i != k else 0 for i in range(1, n+1)}
        
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((w, v))
        
        for _ in range(n):
            for u in graph:
                for w, v in graph[u]:
                    if shortest_path[v] > shortest_path[u] + w:
                        shortest_path[v] = shortest_path[u] + w
        max_val = max(list(shortest_path.values()))
        return max_val if max_val != float('inf') else -1