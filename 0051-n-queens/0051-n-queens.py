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
    def solve(self,col,board,ans,n):
        if col==n:
            ans.append(list(board))
            return 
        
        for row in range(n):
            if self.is_safe(row,col,board,n):
                board[row]=board[row][:col]+'Q'+board[row][col+1:]
                self.solve(col+1,board,ans,n)
                board[row]=board[row][:col]+'.'+board[row][col+1:]

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=['.' *n for _ in range(n)]

        self.solve(0,board,ans,n)
        return ans

        