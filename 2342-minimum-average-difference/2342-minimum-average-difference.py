class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n=len(nums)

        total=sum(nums)
        mini_average=float('inf')
        temp=[0]*n
        left_sum=0
        for i in range(n):
            left_sum+=nums[i]
            if i!=n-1:
                if abs(left_sum//(i+1)-(total-left_sum)//(n-i-1))<mini_average:
                    mini_average=abs(left_sum//(i+1)-(total-left_sum)//(n-i-1))
                    result=i
            else:
                if left_sum//(i+1)<mini_average:
                    result=i
            
        return result
        
        
