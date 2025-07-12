class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m=len(heightMap)
        n=len(heightMap[0])

        heap=[]
        visited=[[False]*n for _ in range(m)]

        directions=[[-1,0],[1,0],[0,-1],[0,1]]

        for i in range(m):
            for j in [0,n-1]:
                heapq.heappush(heap,(heightMap[i][j],i,j))
                visited[i][j]=True
        
        for i in range(n):
            for j in [0,m-1]:
                heapq.heappush(heap,(heightMap[j][i],j,i))
                visited[j][i]=True
        
        answer=0
        while heap:
            h,x,y=heapq.heappop(heap)

            for r,c in directions:
                nr=x+r
                nc=y+c

                if nr in range(m) and nc in range(n) and not visited[nr][nc]:
                    answer+=max(0,h-heightMap[nr][nc])
                    visited[nr][nc]=True
                    heapq.heappush(heap,(max(heightMap[nr][nc],h),nr,nc))

        return answer



        