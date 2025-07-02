class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        visited=set()
        visited.add(1)
        minheap=[]
        heapq.heappush(minheap,1)

        for _ in range(n):
            current=heapq.heappop(minheap)

            for num in primes:
                temp=current*num
                if temp not in visited:
                    visited.add(temp)
                    heapq.heappush(minheap,temp)
        return current
        