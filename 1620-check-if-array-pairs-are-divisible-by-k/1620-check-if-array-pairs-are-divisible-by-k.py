class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n=len(arr)
        if n%2!=0:
            return False
        
        for i in range(n):
            arr[i]=arr[i]%k
        
        count_by_frequency=Counter(arr)
        
        if count_by_frequency[0]%2!=0:
            return False
        if k%2==0 and count_by_frequency[k//2]%2!=0:
            return False
        
        for r in range(1,(k+1)//2):
            if count_by_frequency[r]!=count_by_frequency[k-r]:
                return False
        return True