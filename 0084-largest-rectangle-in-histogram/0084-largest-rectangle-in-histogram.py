class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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





        