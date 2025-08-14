class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=0

        n=len(nums)

        for i in range(n):
            if i>maxi:
                return False
            maxi=max(maxi,i+nums[i])
        return True
        