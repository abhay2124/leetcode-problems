class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        
        def segment_cost(s1: str, s2: str) -> int:
            cnt = [[0] * 26 for _ in range(26)]
            M = 0
            for a, b in zip(s1, s2):
                if a != b:
                    M += 1
                    cnt[ord(a) - 97][ord(b) - 97] += 1
            swaps = 0
            for a in range(26):
                for b in range(a + 1, 26):
                    swaps += min(cnt[a][b], cnt[b][a])
            return M - swaps
        
        # cost[i][j]: min ops to convert word1[i:j+1] -> word2[i:j+1]
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                s1 = word1[i:j+1]
                s2 = word2[i:j+1]
                c_no_rev = segment_cost(s1, s2)
                c_rev = 1 + segment_cost(s1[::-1], s2)
                cost[i][j] = min(c_no_rev, c_rev)
        
        INF = float('inf')
        dp = [0] + [INF] * n
        for i in range(1, n + 1):
            best = INF
            for j in range(i):
                if dp[j] + cost[j][i-1] < best:
                    best = dp[j] + cost[j][i-1]
            dp[i] = best
        
        return dp[n]