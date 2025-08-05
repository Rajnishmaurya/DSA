class Solution:
    def numSub(self, s: str) -> int:
        mod=int(1e9)+7

        answer=0
        temp=0

        n=len(s)

        for i in range(n):
            if s[i]=='0':
                temp=0
            else:
                temp+=1
                answer+=temp
        return answer%mod
        