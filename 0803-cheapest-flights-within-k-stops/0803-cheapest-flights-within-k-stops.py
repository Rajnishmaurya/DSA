class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist=[int(1e9) for _ in range(n)]

        adj_list={}
        for i in range(n):
            adj_list[i]=[]
        
        for x,y,z in flights:
            adj_list[x].append((y,z))

        q=deque()
        q.append((0,src,0)) # steps,source,distance

        while q:
            step,source,cost=q.popleft()

            if step>k:
                continue
            
            for node, price in adj_list[source]:
                temp=price+cost
                if temp<dist[node] and step<=k:
                    dist[node]=temp
                    q.append((step+1,node,temp))
        if dist[dst]!=int(1e9):
            return dist[dst]
        else:
            return -1
        