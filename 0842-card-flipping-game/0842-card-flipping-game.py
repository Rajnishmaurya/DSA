class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:

        n=len(fronts)
        same=set()
        for i in range(n):
            if fronts[i]==backs[i]:
                same.add(fronts[i])
        
        candidate=fronts+backs

        valid=[num for num in candidate if num not in same]

        if not valid:
            return 0
        else:
            return min(valid)
