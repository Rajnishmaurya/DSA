class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list={}
        for i in range(1,n+1):
            adj_list[i]=[]
        
        for x,y,z in times:
            adj_list[x].append((y,z))
        
        dist=[float('inf') for _ in range(n+1)]
        dist[k]=0
        ways=[0]*(n+1)
        ways[k]=1
        heap=[(0,k)]  # distance,source
        mod=int(1e9)
        while heap:
            distance,node=heapq.heappop(heap)

            for y,z in adj_list[node]:
                if z+distance<dist[y]:
                    dist[y]=z+distance
                    heapq.heappush(heap,(z+distance,y))
                    ways[y]=ways[node]
                if z+distance==dist[y]:
                    ways[y]=(ways[y]+ways[node])%mod
        maxi=max(dist[1:])
        return -1 if maxi==float('inf') else maxi

        
        