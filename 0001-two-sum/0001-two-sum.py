class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp={}

        for i , num in enumerate(nums):
            k=target-num
            if k in temp:
                return [temp[k],i]
            temp[num]=i
        return []
        