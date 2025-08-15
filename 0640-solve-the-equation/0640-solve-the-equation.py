class Solution:
    def solveEquation(self, equation: str) -> str:

        def parse(exp):
            x_coef=0
            i=0
            num=0
            sign=1
            while i<len(exp):
                if exp[i]=='+':
                    sign=1
                    i+=1
                elif exp[i]=='-':
                    sign=-1
                    i+=1
                else:
                    j=i
                    while j<len(exp) and exp[j] not in ['+','-']:
                        j+=1
                    term=exp[i:j]

                    if 'x' in term:
                        coef=term.replace('x','')
                        if coef=='':
                            coef='1'
                        elif coef=='-':
                            coef='-1'
                        x_coef+=sign*int(coef)
                    else:
                        num+=sign*int(term)
                    i=j
            return x_coef,num

        

        left,right=equation.split('=')

        left_x,left_num=parse(left)
        right_x,right_num=parse(right)

        coef=left_x-right_x
        const=right_num-left_num

        if coef==0:
            if const==0:
                return "Infinite solutions"
            else:
                return "No solution"
        return "x="+str(const//coef)
        