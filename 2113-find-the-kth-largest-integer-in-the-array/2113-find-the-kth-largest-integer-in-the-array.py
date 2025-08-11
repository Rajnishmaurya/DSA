class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        heap=[]

        n=len(nums)

        for i in range(n):
            heapq.heappush(heap,-int(nums[i]))
        
        while k>1:
            heapq.heappop(heap)
            k-=1
        
        return str(abs(heap[0]))
        