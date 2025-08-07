class Solution:

    def fun(self,index,target,nums,dp):
        if index==0:
            if target==0 and nums[index]==0:
                return 2
            if target==0 or target==nums[index]:
                return 1
            return 0

        if dp[index][target]!=-1:
            return dp[index][target]
        not_taken=self.fun(index-1,target,nums,dp)
        
        taken=False
        if nums[index]<=target:
            taken=self.fun(index-1,target-nums[index],nums,dp)

        dp[index][target]=not_taken + taken
        return dp[index][target]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n=len(nums)
        total=sum(nums)

        if total<target:
            return 0

        if (total-target)%2==1:
            return 0
        
        s2=(total-target)//2

        dp=[[-1 for _ in range(s2+1)] for _ in range(n)]

        return self.fun(n-1,s2,nums,dp)
        