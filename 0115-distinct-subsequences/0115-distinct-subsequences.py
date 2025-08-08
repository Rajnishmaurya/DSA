class Solution:
    def solve(self,m,n,s,t,dp):
        if n<0:
            return 1
        if m<0:
            return 0
        if dp[m][n]!=-1:
            return dp[m][n]
        
        if s[m]==t[n]:
            a=self.solve(m-1,n-1,s,t,dp)
            b=self.solve(m-1,n,s,t,dp)
            dp[m][n]=a+b
            return dp[m][n]
        else:
            dp[m][n]=self.solve(m-1,n,s,t,dp)
            return dp[m][n]


    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s),len(t)

        dp=[[-1]*n for _ in range(m)]

        return self.solve(m-1,n-1,s,t,dp)