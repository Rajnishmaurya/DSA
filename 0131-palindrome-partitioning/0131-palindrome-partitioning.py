class Solution:
    def isPalindrome(self,s):
        left=0
        right=len(s)-1

        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    def solve(self,index,s,temp,result):
        if index==len(s):
            result.append(temp[:])
            return
        
        for i in range(index,len(s)):
            if self.isPalindrome(s[index:i+1]):
                temp.append(s[index:i+1])
                self.solve(i+1,s,temp,result)
                temp.pop()
        return


    def partition(self, s: str) -> List[List[str]]:
        result=[]
        temp=[]
        self.solve(0,s,temp,result)
        return result