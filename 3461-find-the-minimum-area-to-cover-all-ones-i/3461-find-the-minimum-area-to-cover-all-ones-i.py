class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        top, down, left, right = m, -1, n, -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    top = min(top, i)
                    down = max(down, i)
                    left = min(left, j)
                    right = max(right, j)

        return (down - top + 1) * (right - left + 1)