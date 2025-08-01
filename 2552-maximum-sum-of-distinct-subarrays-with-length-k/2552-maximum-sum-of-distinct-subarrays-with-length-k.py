class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum=0
        current_sum=0
        st=set()
        start=0

        for i in range(len(nums)):
            while nums[i] in st or i-start+1>k:
                st.remove(nums[start])
                current_sum-=nums[start]
                start+=1
                
            st.add(nums[i])
            current_sum+=nums[i]
            if i-start+1==k:
                max_sum=max(max_sum,current_sum)
                
        return max_sum
        