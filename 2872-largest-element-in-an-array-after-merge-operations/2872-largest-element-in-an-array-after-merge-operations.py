class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        answer=0
        n=len(nums)

        for i in range(n-1,-1,-1):
            if nums[i]<=answer:
                answer+=nums[i]
            else:
                answer=nums[i]
                
        return answer
        