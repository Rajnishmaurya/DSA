class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(haystack)
        m=len(needle)

        if m==0:
            return 0

        for i in range(n-m+1):
            for k in range(m):
                if haystack[i+k]!=needle[k]:
                    break
            else:
                return i
        return -1
                    
        