class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max=nums[0]
        overall_max=nums[0]
        answer=0

        for i in range(1,len(nums)):
            overall_max=max(overall_max,nums[i])
            if nums[i]<left_max:
                left_max=overall_max
                answer=i
        return answer+1
        