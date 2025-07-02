class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        minheap=[]
        result=0
        temp=0

        for e ,s in sorted(zip(efficiency,speed),reverse=1):
            temp+=s
            heapq.heappush(minheap,s)

            if len(minheap)>k:
                temp-=heapq.heappop(minheap)
            result=max(result,temp*e)
        return result%(int(1e9)+7)
        