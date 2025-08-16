class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        A=[]
        m,n=len(grid),len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    A.append((i,j))
        
        visited=[[0]*n for _ in range(m)]
        distance=[[0]*n for _ in range(m)]
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        depth=0
        while A:
            B=[]

            for x,y in A:
                if not visited[x][y]:
                    visited[x][y]=1
                    distance[x][y]=depth

                    for dx,dy in directions:
                        new_x=x+dx
                        new_y=y+dy

                        if new_x in range(m) and new_y in range(n) and not visited[new_x][new_y]:
                            B.append((new_x,new_y))
            A=B
            depth+=1
        visited=[[0]*n  for _ in range(m)]
        heap=[(-distance[0][0],0,0)]

        while heap:
            dis,i,j=heapq.heappop(heap)
            if visited[i][j]:
                continue
            visited[i][j]=1
            if i==m-1 and j==n-1:
                return abs(dis)
            
            for x,y in directions:
                new_x=i+x
                new_y=j+y

                if new_x in range(m) and new_y in range(n):
                    heapq.heappush(heap,(-min(-dis,distance[new_x][new_y]),new_x,new_y))
        return -1



        