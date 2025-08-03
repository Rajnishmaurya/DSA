class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        ans=0
        end=n-1

        for start in range(n//2-1,-1,-1):
            if 2*nums[start]<=nums[end]:
                ans+=2
                end-=1
        return ans
        