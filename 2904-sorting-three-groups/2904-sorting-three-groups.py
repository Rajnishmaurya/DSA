class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n=len(nums)
        ans=[nums[0]]

        for i in range(1,n):
            if nums[i]>=ans[-1]:
                ans.append(nums[i])
            else:
                index=bisect.bisect_right(ans,nums[i])
                ans[index]=nums[i]
        return n-len(ans)
        