class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n=len(arr1)
        answer=0
        directions=[(1,1),(1,-1),(-1,1),(-1,-1)]

        for x,y in directions:
            max_val=float('-inf')
            min_val=float('inf')

            for i in range(n):
                value=x*arr1[i]+y*arr2[i]+i
                max_val=max(max_val,value)
                min_val=min(min_val,value)
                answer=max(answer,max_val-min_val)
        return answer 


        