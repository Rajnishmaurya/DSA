class Solution:
    def is_safe(self,row,col,board,n):
        i,j=row,col

        while i>=0 and j>=0:
            if board[i][j]=='Q':
                return False
            i-=1
            j-=1
        
        i,j=row,col
        while j>=0:
            if board[i][j]=='Q':
                return False
            j-=1
        
        i,j=row,col
        while i<n and j>=0:
            if board[i][j]=='Q':
                return False
            i+=1
            j-=1
        return True
    def solve(self,col,board,n,count):
        if col==n:
            count[0]+=1
            return 
        
        for row in range(n):
            if self.is_safe(row,col,board,n):
                board[row]=board[row][:col]+'Q'+board[row][col+1:]
                self.solve(col+1,board,n,count)
                board[row]=board[row][:col]+'.'+board[row][col+1:]

    def totalNQueens(self, n: int) -> int:
        count=[0]
        board=['.' *n for _ in range(n)]

        self.solve(0,board,n,count)
        return count[0]

        