class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        for i in range(len(nums)):
            nums[i]=str(nums[i])

        nums.sort(reverse=True, key=lambda x:x*10)

        result="".join(nums)
        return "0" if result[0]=="0" else result
        