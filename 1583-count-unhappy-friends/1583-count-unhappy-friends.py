class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        partner = [0] * n
        for x, y in pairs:
            partner[x] = y
            partner[y] = x
        
        rank = [[0] * n for _ in range(n)]
        for i in range(n):
            for pos, f in enumerate(preferences[i]):
                rank[i][f] = pos
        
        unhappy_count = 0
        
        for x in range(n):
            y = partner[x]
            for u in preferences[x]:
                if rank[x][u] >= rank[x][y]:
                    break 
                v = partner[u]
                if rank[u][x] < rank[u][v]:
                    unhappy_count += 1
                    break
        
        return unhappy_count