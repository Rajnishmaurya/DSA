class Solution:
    def is_prime(self,n):
        if n<2:
            return False
        for i in range(2,int(sqrt(n))+1):
            if n%i==0:
                return False
        return True
    def splitArray(self, nums: List[int]) -> int:
        total=sum(nums)
        n=len(nums)
        temp=0
        temp1=0
        for i in range(len(nums)):
            if self.is_prime(i):
                temp+=nums[i]
            else:
                temp1+=nums[i]    
        return abs(temp-temp1)

        