class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for n in range(num//2,num+1):
            str1=str(n)
            str2=str1[::-1]
            if int(str1)+int(str2)==num:
                return True
        return False
        