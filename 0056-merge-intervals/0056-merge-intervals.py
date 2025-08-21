class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n=len(intervals)
        ans=[]
        ans.append(intervals[0])

        for i in range(1,n):
            if ans and ans[-1][1]<intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1]=max(ans[-1][1],intervals[i][1])
            
        return ans