class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        answer=0
        n=len(nums)
        for i in range(n):
            mini=int(1e9)
            maxi=-int(1e9)
            for j in range(i,n):
                mini=min(mini,nums[j])
                maxi=max(maxi,nums[j])
                answer+=maxi-mini
        return answer
        