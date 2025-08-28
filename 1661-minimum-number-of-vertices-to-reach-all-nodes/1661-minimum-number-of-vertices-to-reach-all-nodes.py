class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree=[0]*n

        for x,y in edges:
            indegree[y]+=1

        result=[]
        for node in range(n):
            if indegree[node]==0:
                result.append(node)
                
        return result