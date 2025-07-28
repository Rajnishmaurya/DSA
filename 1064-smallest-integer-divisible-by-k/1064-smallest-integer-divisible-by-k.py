class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        hit=[False]*k
        n,ans=0,0

        while True:
            ans+=1
            n=(n*10+1)%k
            if n==0:
                return ans
            if hit[n]:
                return -1
            hit[n]=True
        