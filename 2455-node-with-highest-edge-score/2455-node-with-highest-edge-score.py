class Solution:
    def edgeScore(self, edges: List[int]) -> int:

        n = len(edges)
        count = defaultdict(int)
        ans = 0
    
        for i in range(n):
            count[edges[i]] += i

        m = max(count.values())

        for i in range(n):
            if count[i] == m:
                ans = i
                break
        
        return ans
        