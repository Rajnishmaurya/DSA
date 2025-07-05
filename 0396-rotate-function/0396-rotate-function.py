class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)

        dp=[0]*n
        temp=0
        for i , num in enumerate(nums):
            temp+=i*num
        
        dp[0]=temp

        for i in range(1,n):
            dp[i]=dp[i-1]+total-n*nums[n-i]
        return max(dp)
        