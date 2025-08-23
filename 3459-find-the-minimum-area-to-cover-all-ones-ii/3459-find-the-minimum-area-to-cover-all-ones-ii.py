from functools import lru_cache
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        @lru_cache()
        def area(top: int, bottom: int, left: int, right: int) -> int:
            while top <= bottom and all(grid[top][c] == 0 for c in range(left, right + 1)):
                top += 1

            while bottom >= top and all(grid[bottom][c] == 0 for c in range(left, right + 1)):
                bottom -= 1

            while left <= right and all(grid[r][left] == 0 for r in range(top, bottom + 1)):
                left += 1

            while right >= left and all(grid[r][right] == 0 for r in range(top, bottom + 1)):
                right -= 1

            if top > bottom or left > right:
                return 0

            return (bottom - top + 1) * (right - left + 1)

        @lru_cache()
        def sol(l, r, t, b, count):
            if count == 1:
                return area( l, r, t, b)

            ans = float('inf')

            for k in range(l, r):
                ans = min(ans,
                          area( k + 1, r, t, b) + sol(l, k, t, b, count - 1),
                          area( l, k, t, b) + sol(k + 1, r, t, b, count - 1))

            for k in range(t, b):
                ans = min(ans,
                          area(l, r, k + 1, b) + sol(l, r, t, k, count - 1),
                          area( l, r, t, k) + sol(l, r, k + 1, b, count - 1))

            return ans

        return sol(0, rows - 1, 0, cols - 1, 3)