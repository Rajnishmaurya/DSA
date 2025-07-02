class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        dq=deque()
        dq.append((0,0))

        # direction format: [dir_num, row_offset, col_offset]
        directions=[[1,0,1],[2,0,-1],[3,1,0],[4,-1,0]]

        cost=[[float('inf') for _ in range(n)] for _ in range(m)]
        cost[0][0]=0

        while dq:
            row,col=dq.popleft()

            if row==m-1 and col==n-1:
                return cost[row][col]
            
            for direction,r,c in directions:
                nr=r+row
                nc=c+col

                if nr in range(m) and nc in range(n):
                    if grid[row][col]==direction:
                        if cost[nr][nc]>cost[row][col]:
                            cost[nr][nc]=cost[row][col]
                            dq.appendleft((nr,nc))
                    else:
                        if cost[nr][nc]>cost[row][col]+1:
                            cost[nr][nc]=cost[row][col]+1
                            dq.append((nr,nc))
        return -1

                
        