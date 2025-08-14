class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l,r=0,0
        m,n=len(g),len(s)
        g.sort()
        s.sort()
        while l<m and r<n:
            if g[l]<=s[r]:
                l+=1
            r+=1
        return l
