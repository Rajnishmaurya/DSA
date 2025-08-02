class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])

        row=[0]*m
        col=[0]*n

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    row[i]+=1
                    col[j]+=1
        answer=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    answer+=(row[i]-1)*(col[j]-1)
        return answer
        