class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp=[[0]*(n+1) for _ in range(m+1)]

        for s in strs:
            zero=s.count('0')
            ones=s.count('1')

            for i in range(m,zero-1,-1):
                for j in range(n,ones-1,-1):
                    dp[i][j]=max(dp[i][j], 1+dp[i-zero][j-ones])
        return dp[m][n]
        