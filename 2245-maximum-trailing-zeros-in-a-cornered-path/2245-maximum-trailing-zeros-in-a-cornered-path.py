from typing import List

class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def count_factor(x, f):
            cnt = 0
            while x % f == 0:
                x //= f
                cnt += 1
            return cnt
        
        cnt2 = [[0]*n for _ in range(m)]
        cnt5 = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                cnt2[i][j] = count_factor(grid[i][j], 2)
                cnt5[i][j] = count_factor(grid[i][j], 5)
        
        # prefix sums in 4 directions (inclusive of current cell)
        left2 = [[0]*n for _ in range(m)]
        left5 = [[0]*n for _ in range(m)]
        right2 = [[0]*n for _ in range(m)]
        right5 = [[0]*n for _ in range(m)]
        up2 = [[0]*n for _ in range(m)]
        up5 = [[0]*n for _ in range(m)]
        down2 = [[0]*n for _ in range(m)]
        down5 = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                left2[i][j] = cnt2[i][j] + (left2[i][j-1] if j > 0 else 0)
                left5[i][j] = cnt5[i][j] + (left5[i][j-1] if j > 0 else 0)
        
        for i in range(m):
            for j in range(n-1, -1, -1):
                right2[i][j] = cnt2[i][j] + (right2[i][j+1] if j < n-1 else 0)
                right5[i][j] = cnt5[i][j] + (right5[i][j+1] if j < n-1 else 0)
        
        for j in range(n):
            for i in range(m):
                up2[i][j] = cnt2[i][j] + (up2[i-1][j] if i > 0 else 0)
                up5[i][j] = cnt5[i][j] + (up5[i-1][j] if i > 0 else 0)
        
        for j in range(n):
            for i in range(m-1, -1, -1):
                down2[i][j] = cnt2[i][j] + (down2[i+1][j] if i < m-1 else 0)
                down5[i][j] = cnt5[i][j] + (down5[i+1][j] if i < m-1 else 0)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                c2, c5 = cnt2[i][j], cnt5[i][j]
                combos = [
                    (left2[i][j] + up2[i][j] - c2, left5[i][j] + up5[i][j] - c5),
                    (left2[i][j] + down2[i][j] - c2, left5[i][j] + down5[i][j] - c5),
                    (right2[i][j] + up2[i][j] - c2, right5[i][j] + up5[i][j] - c5),
                    (right2[i][j] + down2[i][j] - c2, right5[i][j] + down5[i][j] - c5),
                ]
                for t2, t5 in combos:
                    ans = max(ans, min(t2, t5))
        
        return ans


# ---------- Quick tests ----------
if __name__ == "__main__":
    sol = Solution()

    grid1 = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
    print(sol.maxTrailingZeros(grid1))  # Expected: 3

    grid2 = [[4,3,2],[7,6,1],[8,8,8]]
    print(sol.maxTrailingZeros(grid2))  # Expected: 0