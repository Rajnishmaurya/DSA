class Solution:
    def solve(self,s,wordDict,start,curr,ans):
        if start==len(s):
            ans.append(' '.join(curr))
        
        for i in range(start,len(s)):
            word=s[start:i+1]
            if word in wordDict:
                curr.append(word)
                self.solve(s,wordDict,i+1,curr,ans)
                curr.pop()

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans=[]
        self.solve(s,set(wordDict),0,[],ans)
        return ans
        