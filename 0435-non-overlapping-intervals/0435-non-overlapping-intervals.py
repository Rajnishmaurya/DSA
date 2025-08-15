class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        n=len(intervals)
        end=intervals[0][1]

        for i in range(1,n):
            if intervals[i][0]<end:
                count+=1
                end=min(end,intervals[i][1])
            else:
                end=intervals[i][1]

        return count
        