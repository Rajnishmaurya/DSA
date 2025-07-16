class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r=radius
        self.x=x_center
        self.y=y_center
        
    def randPoint(self) -> List[float]:
        thetha=uniform(0,2*pi)
        r=sqrt(uniform(0,self.r**2))

        return self.x+r*cos(thetha), self.y+r*sin(thetha)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()