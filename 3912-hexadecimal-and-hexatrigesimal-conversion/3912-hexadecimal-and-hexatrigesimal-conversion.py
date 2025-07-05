class Solution:
    def solve(self, num):
        chars="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if num==0:
            return "0"
        result=""
        while num>0:
            result=chars[num%36]+result
            num//=36

        return result
    def concatHex36(self, n: int) -> str:
        temp2=n*n
        temp3=n*n*n

        hexa=hex(temp2)[2:].upper()
        hexa1=self.solve(temp3)

        return hexa+hexa1
        
        