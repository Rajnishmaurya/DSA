class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        result=[]

        count=Counter(barcodes)

        heap=[[-v,k] for k ,v in count.items()]
        
        heapq.heapify(heap)

        while heap:
            a=heapq.heappop(heap)
            result.append(a[1])
            if heap:
                b=heapq.heappop(heap)
                result.append(b[1])

                if abs(b[0])>1:
                    heapq.heappush(heap,[b[0]+1,b[1]])
            if abs(a[0])>1:
                heapq.heappush(heap,[a[0]+1,a[1]])
        return result
