class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cz=0
        co=0
        l=0
        r=0
        m=0
        for i in range(len(nums)):
              
            if nums[i]==0:
                cz+=1
            if cz>1:
                break
            r+=1
            m=max(m,r-l)
        while r<len(nums)-1:
            if nums[r+1]==0:
                cz+=1
            if cz>1:
                while cz>1:
                    if nums[l]==0:
                        cz-=1
                    l+=1
                r+=1
            else:
                r+=1
            m=max(m,r-l+1)
        return m-1