class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)

        dp=[1]*n
        hash_index=list(range(n))

        for i in range(n):
            for prev in range(i):
                if nums[i]%nums[prev]==0 and 1+dp[prev]>dp[i]:
                    dp[i]=1+dp[prev]
                    hash_index[i]=prev
        
        ans=-1
        last_index=-1

        for i in range(n):
            if dp[i]>ans:
                ans=dp[i]
                last_index=i

        result=[nums[last_index]]

        while hash_index[last_index]!=last_index:
            last_index=hash_index[last_index]
            result.append(nums[last_index])
        return result


        