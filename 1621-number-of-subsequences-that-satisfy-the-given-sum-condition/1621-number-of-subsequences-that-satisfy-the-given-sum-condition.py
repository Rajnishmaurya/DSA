class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        result=0
        nums.sort()
        start=0
        end=len(nums)-1

        while start<=end:
            temp=nums[start]+nums[end]
            if temp>target:
                end-=1
            else:
                result+=pow(2,(end-start))
                result=result%(int(1e9)+7)
                start+=1
        return result
        