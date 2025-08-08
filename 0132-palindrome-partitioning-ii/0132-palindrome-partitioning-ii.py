class Solution:
    # def is_palindrome(self,i,j,s):
    #     while i<j:
    #         if s[i]!=s[j]:
    #             return False
    #         i+=1
    #         j-=1
    #     return True
    def solve(self,i,n,s,dp,palindrome):
        if i==n:
            return 0
        if dp[i]!=-1:
            return dp[i]
        
        mini=float('inf')
        for j in range(i,n):
            if palindrome[i][j]:
                cost=1+self.solve(j+1,n,s,dp,palindrome)
                mini=min(mini,cost)
        dp[i]=mini
        return dp[i]
    def minCut(self, s: str) -> int:
        n=len(s)
        dp=[-1]*n
        palindrome=[[False]*n for _ in range(n)]
        for start in range(n,-1,-1):
            for end in range(start,n):
                if s[start]==s[end] and (end-start<=2 or palindrome[start+1][end-1]):
                    palindrome[start][end]=True

        return self.solve(0,n,s,dp,palindrome)-1
        