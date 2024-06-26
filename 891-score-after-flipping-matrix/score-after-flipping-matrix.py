class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0

        for j in range(m):
            set_count = 0
            for i in range(n):
                set_count += grid[i][j]==grid[i][0]
            res += max(set_count, n - set_count) * (1 << (m - 1 - j))

        return res