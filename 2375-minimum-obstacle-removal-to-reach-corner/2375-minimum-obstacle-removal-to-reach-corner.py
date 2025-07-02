class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        minheap=[]
        heapq.heappush(minheap,(0,0,0))
        directions=[[1,0],[-1,0],[0,1],[0,-1]]

        result=0
        while minheap:
            step,row,col=heappop(minheap)
            if grid[row][col]==-1:
                continue
            grid[row][col]=-1
            if row==m-1 and col==n-1:
                result=step
                break
            
            for r,c in directions:
                nr=r+row
                nc=c+col
                if nr in range(m) and nc in range(n) and grid[nr][nc]!=-1:
                    if grid[nr][nc]==0:
                        heapq.heappush(minheap,(step,nr,nc))
                    else:
                        heapq.heappush(minheap,(step+1,nr,nc))
        return result
                

        