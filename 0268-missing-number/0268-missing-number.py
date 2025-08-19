class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp=len(nums)

        for i , num in enumerate(nums):
            temp^=i^num        
        return temp
        