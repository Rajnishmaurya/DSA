class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd,even,both=0,0,0
        flag=nums[0]%2

        for num in nums:
            if num%2==0:
                even+=1
            else:
                odd+=1
            if num%2==flag:
                both+=1
                flag=1-flag
        return max(both,odd,even)