class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n=len(maze),len(maze[0])

        q=deque()
        q.append((entrance[0],entrance[1],0))
        maze[entrance[0]][entrance[1]]='+'

        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            r,c,steps=q.popleft()

            for dr,dc in directions:
                nr,nc=r+dr,c+dc

                if nr in range(m) and nc in range(n) and maze[nr][nc]=='.':
                    if nr==0 or nr==m-1 or nc==0 or nc==n-1:
                        return steps+1
                    maze[nr][nc]='+'
                    q.append((nr,nc,steps+1))
        return -1

        