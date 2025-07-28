class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()

        count=Counter(arr)
        res=0
        i,l=0,len(arr)

        while i<l:
            j,k=i,l-1
            while j<k:
                temp=arr[i]+arr[j]+arr[k]
                if temp<target:
                    j+=count[arr[j]]
                elif temp>target:
                    k-=count[arr[k]]
                else:
                    if arr[i]!=arr[j]!=arr[k]:
                        res+=count[arr[i]]*count[arr[j]]*count[arr[k]]
                    elif arr[i]==arr[j]!=arr[k]:
                        res+=count[arr[i]]*(count[arr[i]]-1)*count[arr[k]]//2
                    elif arr[i]!=arr[j]==arr[k]:
                        res+=count[arr[i]]*(count[arr[j]])*(count[arr[k]]-1)//2
                    else:
                        res+=count[arr[i]]*(count[arr[i]]-1)*(count[arr[k]]-2)//6
                    j+=count[arr[j]]
                    k-=count[arr[k]]
            i+=count[arr[i]]
        return res%1000000007
        