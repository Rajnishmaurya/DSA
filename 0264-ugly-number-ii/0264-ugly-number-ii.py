class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2,i3,i5=0,0,0
        ugly=[1]

        for i in range(1,n):
            n2,n3,n5=ugly[i2]*2,ugly[i3]*3,ugly[i5]*5
            nex=min(n2,n3,n5)
            ugly.append(nex)
            if nex==ugly[i2]*2:
                i2+=1
            if nex==ugly[i3]*3:
                i3+=1
            if nex==ugly[i5]*5:
                i5+=1
        return ugly[-1]

        