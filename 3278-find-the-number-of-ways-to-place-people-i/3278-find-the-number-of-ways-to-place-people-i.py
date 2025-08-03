class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n=len(points)
        count=0

        for i in range(n):
            ax,ay=points[i]
            for j in range(n):
                if i==j:
                    continue
                bx,by=points[j]

                if ax<=bx and ay>=by:
                    found=False

                    for k in range(n):
                        if k!=i and k!=j:
                            cx,cy=points[k]

                            if ax<=cx<=bx and ay>=cy>=by:
                                found=True
                                break
                    
                    if not found:
                        count+=1

        return count
        