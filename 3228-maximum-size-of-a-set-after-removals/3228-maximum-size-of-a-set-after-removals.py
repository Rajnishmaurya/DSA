class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)//2
        nums1=set(nums1)
        nums2=set(nums2)

        common=nums1 & nums2

        v1=min(len(nums1)-len(common),n)
        v2=min(len(nums2)-len(common),n)

        return min(v1+v2+len(common),2*n)




        