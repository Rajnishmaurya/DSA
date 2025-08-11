class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        answer=set()
        x_list=[]

        temp=1

        while temp<=bound:
            x_list.append(temp)
            if x==1:
                break
            temp*=x
        
        temp=1
        y_list=[]
        while temp<=bound:
            y_list.append(temp)
            if y==1:
                break
            temp*=y
        
        for x in x_list:
            for y in y_list:
                if x+y <=bound:
                    answer.add(x+y)


        return list(answer)
        