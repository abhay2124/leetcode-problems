from collections import deque
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))  

        visited = [False] * n
        visited[0] = True
        queue = deque([0])
        changes = 0

        while queue:
            u = queue.popleft()
            for v, cost in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    changes += cost
                    queue.append(v)

        return changes