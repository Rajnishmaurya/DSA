class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        answer=1
        while left<=right:
            total_hour=0
            mid=(left+right)//2

            for banana in piles:
                if banana%mid==0:
                    total_hour+=banana//mid
                else:
                    total_hour+=banana//mid+1
            if total_hour<=h:
                answer=mid
                right=mid-1
            else:
                left=mid+1
        return answer


        