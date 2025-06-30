class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        st=set(nums)

        temp=1

        while True:
            if temp not in st:
                break
            temp+=1
        return temp

        