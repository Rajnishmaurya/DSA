class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        result=float(1e9)
        nums.sort()
        for i in range(n-2):
            left,right=i+1,n-1
            while left<right:
                temp=nums[i]+nums[left]+nums[right]
                if temp==target:
                    return temp
                elif temp<target:
                    left+=1
                else:
                    right-=1
                if abs(temp-target)<=abs(result-target):
                    result=temp
        return result
        