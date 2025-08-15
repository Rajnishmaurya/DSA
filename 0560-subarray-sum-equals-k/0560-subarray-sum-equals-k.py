class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        value=defaultdict(int)

        value[0]=1

        ans=0

        for num in nums:
            prefix_sum+=num
            target=prefix_sum-k
            if target in value:
                ans+=value[target]
            value[prefix_sum]+=1
        return ans
        