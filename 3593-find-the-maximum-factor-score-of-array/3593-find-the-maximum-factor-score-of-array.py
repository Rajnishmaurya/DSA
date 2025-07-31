class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n=len(nums)
        count=Counter(nums)

        result=gcd(*nums)*lcm(*nums)

        for i in range(n):
            if count[nums[i]]>1:
                continue
            arr=nums[:i]+nums[i+1:]
            result=max(result,gcd(*arr)*lcm(*arr))
        return result
        