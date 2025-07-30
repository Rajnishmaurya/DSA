class Solution:
    def maxDiff(self, num: int) -> int:
        s_num=str(num)

        a=s_num

        for i in range(len(s_num)):
            if s_num[i]!="9":
                break

        a=a.replace(s_num[i],"9")

        b=s_num

        if s_num[0]=="1":
            for i in range(1,len(s_num)):
                if s_num[i]!="0" and s_num[i]!="1":
                    b=s_num.replace(s_num[i],"0")
                    break
        else:
            b=s_num.replace(s_num[0],"1")
        return int(a)-int(b)

        