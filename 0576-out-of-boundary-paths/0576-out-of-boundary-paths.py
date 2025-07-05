from collections import deque
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove==0:
            return 0
        mod=int(1e9)+7
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        result=0

        #dp[step][row][col]
        dp=[[[0 for _ in range(n)] for _ in range(m)] for _ in range(maxMove+1)]
        dp[0][startRow][startColumn]=1
        
        for step in range(maxMove):
            for i in range(m):
                for j in range(n):
                    if dp[step][i][j]>0:
                        for dr,dc in directions:
                            nr=dr+i
                            nc=dc+j
                            if nr in range(m) and nc in range(n):
                                dp[step+1][nr][nc]=(dp[step+1][nr][nc]+dp[step][i][j])%mod
                            else:
                                result=(result+dp[step][i][j])%mod
        return result