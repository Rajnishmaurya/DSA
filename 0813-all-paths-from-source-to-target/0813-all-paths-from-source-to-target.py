class Solution:
    def solve(self,result,temp,graph,node,n):
        if node==n-1:
            result.append(temp[:])
            return
        for i in graph[node]:
            temp.append(i)
            self.solve(result,temp,graph,i,n)
            temp.pop()
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result=[]
        temp=[]
        temp.append(0)
        n=len(graph)
        self.solve(result,temp,graph,0,n)
        return result
        