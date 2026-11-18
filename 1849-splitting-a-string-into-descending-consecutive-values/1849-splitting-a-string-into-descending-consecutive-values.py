class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)

        def dfs(start: int, prev: int) -> bool:
            if start == n:
                return True
            val = 0
            for end in range(start, n):
                val = val * 10 + int(s[end])
                if val > prev - 1:
                    break  # values only grow as we extend
                if val == prev - 1 and dfs(end + 1, val):
                    return True
            return False

        val = 0
        for i in range(n - 1): 
            val = val * 10 + int(s[i])
            if dfs(i + 1, val):
                return True
        return False