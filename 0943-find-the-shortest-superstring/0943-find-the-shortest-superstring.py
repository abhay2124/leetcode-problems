from typing import List

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)

        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                a, b = words[i], words[j]
                for k in range(min(len(a), len(b)), 0, -1):
                    if a.endswith(b[:k]):
                        overlap[i][j] = k
                        break

        full = 1 << n
        NEG = -1
        dp = [[NEG] * n for _ in range(full)]
        parent = [[-1] * n for _ in range(full)]
        for i in range(n):
            dp[1 << i][i] = 0

        for mask in range(full):
            for last in range(n):
                if dp[mask][last] < 0:
                    continue
                for nxt in range(n):
                    if mask & (1 << nxt):
                        continue
                    nmask = mask | (1 << nxt)
                    val = dp[mask][last] + overlap[last][nxt]
                    if val > dp[nmask][nxt]:
                        dp[nmask][nxt] = val
                        parent[nmask][nxt] = last

        mask = full - 1
        last = max(range(n), key=lambda j: dp[mask][j])

        order = []
        while last != -1:
            order.append(last)
            prev = parent[mask][last]
            mask ^= 1 << last
            last = prev
        order.reverse()

        result = words[order[0]]
        for idx in range(1, len(order)):
            result += words[order[idx]][overlap[order[idx - 1]][order[idx]]:]
        return result