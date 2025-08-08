class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n=len(nums)

        nums.insert(0,1)
        nums.append(1)

        dp=[[-1]*(n+2) for _  in range(n+2)]

        def f(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            maxi=float('-inf')
            for index in range(i,j+1):
                cost = nums[i-1]*nums[index]*nums[j+1] + f(i,index-1) + f(index+1,j)
                maxi=max(maxi,cost)
            dp[i][j]=maxi
            return maxi
        return f(1,n)
        