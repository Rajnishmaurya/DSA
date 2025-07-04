class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x+y <target:
            return False
        return (target%gcd(x,y))==0
        