class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        heap=[]
        n=len(queries)
        result=[-1]*n

        for i in range(n):
            temp=abs(queries[i][0])+abs(queries[i][1])
            if len(heap)>=k:
                heapq.heappushpop(heap,-temp)
            else:
                heapq.heappush(heap,-temp)
            if len(heap)==k:
                result[i]=abs(heap[0])
        return result




        

