class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        answer=0
        n=len(arr)
        mod=int(1e9+7)

        next_smaller=[n]*n
        stack=[]
        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                next_smaller[stack.pop()]=i
            stack.append(i)
        
        stack=[]
        previous_smaller=[-1]*n

        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                previous_smaller[stack.pop()]=i
            stack.append(i)
        
        for i in range(n):
            answer=(answer+ arr[i]*(i-previous_smaller[i])*(next_smaller[i]-i))%mod
        
        return answer