class Solution:
    def countHousePlacements(self, n: int) -> int:
        prev2,prev1=2,1
        mod=int(1e9)+7

        for i in range(1,n):
            temp=prev2+prev1
            prev1=prev2
            prev2=temp
        return (prev2*prev2)%(mod)
        