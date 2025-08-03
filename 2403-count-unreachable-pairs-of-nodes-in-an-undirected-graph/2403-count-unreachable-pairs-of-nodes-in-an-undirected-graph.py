class Solution:
    def dfs(self,node ,visited,graph):
        if visited[node]:
            return 0
        
        visited[node]=True

        return 1+sum(self.dfs(temp,visited,graph) for temp in graph[node] )

    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        graph=[[] for _ in range(n)]

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited=[False]*n

        sizes=[self.dfs(i,visited,graph) for i in range(n)]

        return sum(sizes[i]*(n-sizes[i]) for i in range(n))//2
        