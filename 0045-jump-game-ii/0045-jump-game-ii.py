class Solution:
    def jump(self, nums: List[int]) -> int:
        max_end=0
        end=0
        jump=0

        for i in range(len(nums)-1):
            max_end=max(max_end,i+nums[i])
            if i==end:
                jump+=1
                end=max_end
        return jump
        