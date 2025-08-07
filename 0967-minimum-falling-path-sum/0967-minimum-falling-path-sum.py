class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]

        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(n):
                up = dp[i - 1][j]
                left = dp[i - 1][j - 1] if j > 0 else int(1e9)
                right = dp[i - 1][j + 1] if j < n - 1 else int(1e9)
                dp[i][j] = matrix[i][j] + min(up, left, right)

        return min(dp[n - 1]) 
