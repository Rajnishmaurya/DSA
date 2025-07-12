class Solution:
    def solve(self, s):
        stack =0

        for char in s:
            if char == '(':
                stack+=1
            elif char == ')':
                if stack==0:
                    return False
                stack-=1

        return stack==0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        visited=set()
        answer=[]
        q=deque()
        q.append(s)
        visited.add(s)
        found=False
        while q:
            temp=q.popleft()
            if self.solve(temp):
                answer.append(temp)
                found=True
            
            if found:
                continue
                
            for i in range(len(temp)):
                if temp[i] not in ('(',')'):
                    continue
                next_str=temp[:i]+temp[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    q.append(next_str)

        return answer if answer else [""]
                
        