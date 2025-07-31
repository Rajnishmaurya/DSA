class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        answer=0

        lower=[-1]*26
        upper=[-1]*26

        for i in range(len(word)):
            index=ord(word[i])
            if index>=97:
                lower[index-97]=i
            elif upper[index-65]==-1:
                upper[index-65]=i
        for i in range(26):
            if lower[i]!=-1 and lower[i]<upper[i]:
                answer+=1
        return answer
        
