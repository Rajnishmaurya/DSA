class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        answer=[]
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1

            while j<k:
                total=nums[i]+nums[j]+nums[k]

                if total>0:
                    k-=1
                elif total<0:
                    j+=1
                else:
                    answer.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
        return answer

                    
        