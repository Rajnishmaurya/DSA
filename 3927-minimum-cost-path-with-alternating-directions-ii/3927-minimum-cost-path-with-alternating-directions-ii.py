class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        def cost1(i,j):
            return (i+1)*(j+1)

        directions=[[1,0],[0,1]]

        mini=[(cost1(0,0),0,0,1)]
        visited=set()

        while mini:
            cost,i,j,step=heapq.heappop(mini)

            parity=step%2

            if (i,j, parity) in visited:
                continue
            visited.add((i,j,parity))

            if i==m-1 and j==n-1:
                return cost

            if parity==1:
                for dr,dc in directions:
                    nr=i+dr
                    nc=j+dc

                    if nr in range(m) and nc in range(n):
                        heapq.heappush(mini,(cost+cost1(nr,nc),nr,nc,step+1))
            else:
                heapq.heappush(mini,(cost+waitCost[i][j],i,j,step+1))
        return -1
                        
        