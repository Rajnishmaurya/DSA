class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:

        n=len(colsum)

        matrix=[[0]*n for _ in range(2)]

        if upper + lower !=sum(colsum):
            return []
        
        for i in range(n):
            if colsum[i]==2:
                if lower>0 and upper>0:
                    matrix[0][i]=1
                    matrix[1][i]=1
                    lower-=1
                    upper-=1
                else:
                    return []
        for i in range(n):
            if colsum[i]==1:
                if upper>0:
                    matrix[0][i]=1
                    upper-=1
                elif lower>0:
                    matrix[1][i]=1
                    lower-=1
                else:
                    return []
        if lower==0 and upper==0:
            return matrix
        else:
            return []
