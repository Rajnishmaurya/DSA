class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        count=0
        prev=0
        for num in rungs:
            if num-prev>dist:
                count+=(num-prev-1)//dist
            prev=num
        return count
        