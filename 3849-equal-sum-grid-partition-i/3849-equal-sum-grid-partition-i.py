class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n=len(grid),len(grid[0])

        height=[0]*m
        width=[0]*n

        for i in range(m):
            temp=0
            for j in range(n):
                temp+=grid[i][j]
            height[i]=temp
        
        for i in range(n):
            temp=0
            for j in range(m):
                temp+=grid[j][i]
            width[i]=temp
        
        total=sum(height)
        temp=0

        for i in range(m-1):
            temp+=height[i]
            total-=height[i]
            if total==temp:
                return True
        
        total=sum(width)
        temp=0

        for i in range(n-1):
            temp+=width[i]
            total-=width[i]
            if total==temp:
                return True
        return False
            

        