class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod=int(1e9)+7

        powers=[]
        i=1

        while True:
            temp=i**x
            if temp>n:
                break
            powers.append(temp)
            i+=1
        dp=[0]*(n+1)
        dp[0]=1

        for p in powers:
            for s in range(n,p-1,-1):
                dp[s]=(dp[s]+dp[s-p])%mod
        return dp[n]
        
        