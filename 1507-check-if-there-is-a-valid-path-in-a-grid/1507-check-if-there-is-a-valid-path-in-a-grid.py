class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m,n=len(grid),len(grid[0])

        parent=list(range(m*n))
        rank=[0]*(m*n)

        def find(x):
            if x==parent[x]:
                return x
            else:
                return find(parent[x])
        
        def union(x,y):
            ux=find(x)
            uy=find(y)
            if ux==uy:
                return 
            if rank[ux]<rank[uy]:
                parent[ux]=uy
            elif rank[uy]<rank[ux]:
                parent[uy]=ux
            else:
                parent[ux]=uy
                rank[uy]+=1
        
        def do_union(i1,j1,i2,j2):
            if i1 in range(m) and i2 in range(m) and j1 in range(n) and j2 in range(n):
                union(i1*n+j1,i2*n+j2)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    if j+1<n and grid[i][j+1] in [1,3,5]:
                        do_union(i,j,i,j+1)
                    if j-1>=0 and grid[i][j-1] in [1,4,6]:
                        do_union(i,j,i,j-1)
                elif grid[i][j] == 2:
                    if i + 1 < m and grid[i + 1][j] in [2, 5, 6]:
                        do_union(i, j, i + 1, j)
                    if i - 1 >= 0 and grid[i - 1][j] in [2, 3, 4]:
                        do_union(i, j, i - 1, j)
                elif grid[i][j] == 3:
                    if j - 1 >= 0 and grid[i][j - 1] in [1, 4, 6]:
                        do_union(i, j, i, j - 1)
                    if i + 1 < m and grid[i + 1][j] in [2, 5, 6]:
                        do_union(i, j, i + 1, j)
                elif grid[i][j] == 4:
                    if j + 1 < n and grid[i][j + 1] in [1, 3, 5]:
                        do_union(i, j, i, j + 1)
                    if i + 1 < m and grid[i + 1][j] in [2, 5, 6]:
                        do_union(i, j, i + 1, j)
                elif grid[i][j] == 5:
                    if j - 1 >= 0 and grid[i][j - 1] in [1, 4, 6]:
                        do_union(i, j, i, j - 1)
                    if i - 1 >= 0 and grid[i - 1][j] in [2, 3, 4]:
                        do_union(i, j, i - 1, j)
                elif grid[i][j] == 6:
                    if j + 1 < n and grid[i][j + 1] in [1, 3, 5]:
                        do_union(i, j, i, j + 1)
                    if i - 1 >= 0 and grid[i - 1][j] in [2, 3, 4]:
                        do_union(i, j, i - 1, j)
        return find(0)==find(m*n-1)