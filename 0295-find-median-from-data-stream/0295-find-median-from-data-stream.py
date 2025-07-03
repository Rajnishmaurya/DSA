class MedianFinder:

    def __init__(self):
        self.temp=[]

    def addNum(self, num: int) -> None:
        self.temp.append(num)

    def findMedian(self) -> float:
        n=len(self.temp)
        self.temp.sort()

        if n%2==0:
            return (self.temp[n//2-1]+self.temp[n//2])/2
        else:
            return self.temp[n//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()