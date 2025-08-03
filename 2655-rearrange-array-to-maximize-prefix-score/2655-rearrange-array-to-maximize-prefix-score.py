class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return sum(prefix>0 for prefix in accumulate(nums))
        