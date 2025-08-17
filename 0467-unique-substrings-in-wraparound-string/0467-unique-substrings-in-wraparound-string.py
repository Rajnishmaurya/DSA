class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        max_len_end_with=[0]*26

        curr_len=0

        for i in range(len(s)):
            if i>0 and (ord(s[i])-ord(s[i-1]))%26==1:
                curr_len+=1
            else:
                curr_len=1
            
            index=ord(s[i])-ord('a')
            max_len_end_with[index]=max(max_len_end_with[index],curr_len)
        
        return sum(max_len_end_with)


        