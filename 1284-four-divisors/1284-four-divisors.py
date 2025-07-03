class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result=0

        for num in nums:
            divisor=set()
            for i in range(1, floor(sqrt(num))+1):
                if num%i==0:
                    divisor.add(num//i)
                    divisor.add(i)
                if len(divisor)>4:
                    break
            if len(divisor)==4:
                result+=sum(divisor)
        return result
        