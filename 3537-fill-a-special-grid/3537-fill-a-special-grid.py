class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        def build(n):
            size = 1 << n
            grid = [[0] * size for _ in range(size)]
            if n == 0:
                return grid
            m = size // 2
            sub = build(n - 1)
            block = m * m  # number of cells in each quadrant
            
            # Top-right: offset 0
            # Bottom-right: offset block
            # Bottom-left: offset 2*block
            # Top-left: offset 3*block
            for i in range(m):
                for j in range(m):
                    v = sub[i][j]
                    grid[i][j + m] = v                # top-right
                    grid[i + m][j + m] = v + block     # bottom-right
                    grid[i + m][j] = v + 2 * block     # bottom-left
                    grid[i][j] = v + 3 * block         # top-left
            return grid
        
        return build(n)