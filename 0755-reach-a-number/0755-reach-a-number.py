class Solution:
    def reachNumber(self, target: int) -> int:
        target=abs(target)
        steps=0
        total=0

        while total<target or (total-target)%2!=0:
            steps+=1
            total+=steps
        return steps