class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        result=[-1]*n
        
        for i in range(2*n-1,-1,-1):
            while stack and stack[-1]<=nums[i%n]:
                stack.pop()
            
            if i <n:
                if stack:
                    result[i]=stack[-1]
            stack.append(nums[i%n])
        return result
        