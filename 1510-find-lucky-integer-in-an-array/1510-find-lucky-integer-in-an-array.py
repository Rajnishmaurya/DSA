class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lis=defaultdict(int)

        for num in arr:
            lis[num]+=1
        
        result=-1

        for num in arr:
            if num==lis[num]:
                result=max(result,num)
        return result
        