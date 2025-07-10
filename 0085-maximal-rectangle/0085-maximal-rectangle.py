class Solution:
    def solve(self, heights):
        n=len(heights)
        stack=[]
        leftsmall=[0]*n
        rightsmall=[0]*n
        
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            
            leftsmall[i]=stack[-1]+1 if stack else 0
            stack.append(i)

        while stack:
            stack.pop()
        
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            
            rightsmall[i]=stack[-1]-1 if stack else n-1
            stack.append(i)

        answer=0
        for i in range(n):
            answer=max(answer,heights[i]*(rightsmall[i]-leftsmall[i]+1))
        return answer

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        array = [0] * n
        answer = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    array[j] += 1
                else:
                    array[j] = 0
            answer = max(answer, self.solve(array))

        return answer
