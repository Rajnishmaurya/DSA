class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        freq=[0]*(max(fruits)+1)
        ans, cnt, baskets, l=0, 0, 0, 0
        for r, x in enumerate(fruits):
            freq[x]+=1
            if freq[x]==1: baskets+=1
            cnt+=1
            while baskets>2:
                y=fruits[l]
                freq[y]-=1
                if freq[y]==0: baskets-=1
                l+=1
                cnt-=1
            ans=max(ans, cnt)
        return ans
        