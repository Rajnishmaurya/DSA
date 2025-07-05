import copy
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        matrix=[[1 for _ in range(n)] for _ in range(n)]
        for x,y in mines:
            matrix[x][y]=0

        left = copy.deepcopy(matrix)
        right = copy.deepcopy(matrix)
        top = copy.deepcopy(matrix)
        bottom = copy.deepcopy(matrix)

        for i in range(n):
            for j in range(n):
                x=n-i-1
                y=n-j-1
                if i>0 and top[i][j]:
                    top[i][j]+=top[i-1][j]
                if j>0 and left[i][j]:
                    left[i][j]+=left[i][j-1]
                if x<n-1 and bottom[x][y]:
                    bottom[x][y]+=bottom[x+1][y]
                if y<n-1 and right[x][y]:
                    right[x][y]+=right[x][y+1]
        
        result=0

        for i in range(n):
            for j in range(n):
                result=max(result,min(top[i][j],left[i][j],right[i][j],bottom[i][j]))
        return result
                
