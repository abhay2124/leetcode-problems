import heapq
from collections import defaultdict
from typing import List


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                if ra > rb:
                    ra, rb = rb, ra
                parent[rb] = ra

        # Build union-find from connections
        for u, v in connections:
            union(u, v)

        # Build a min-heap of station ids for each grid (component root)
        heaps = defaultdict(list)
        for i in range(1, c + 1):
            heapq.heappush(heaps[find(i)], i)

        online = [True] * (c + 1)
        res = []

        for t, x in queries:
            if t == 2:
                # Station x goes offline
                online[x] = False
            else:
                # t == 1: maintenance check on station x
                if online[x]:
                    res.append(x)
                else:
                    root = find(x)
                    h = heaps[root]
                    # Lazily discard offline stations from the top of the heap
                    while h and not online[h[0]]:
                        heapq.heappop(h)
                    res.append(h[0] if h else -1)

        return res


# ---------- Quick tests ----------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    c1 = 5
    connections1 = [[1, 2], [2, 3], [3, 4], [4, 5]]
    queries1 = [[1, 3], [2, 1], [1, 1], [2, 2], [1, 2]]
    print(sol.processQueries(c1, connections1, queries1))  # Expected: [3, 2, 3]

    # Example 2
    c2 = 3
    connections2 = []
    queries2 = [[1, 1], [2, 1], [1, 1]]
    print(sol.processQueries(c2, connections2, queries2))  # Expected: [1, -1]