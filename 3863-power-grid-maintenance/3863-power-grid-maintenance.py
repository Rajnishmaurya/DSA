from typing import List
from collections import defaultdict
from sortedcontainers import SortedSet

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c)
        for u, v in connections:
            uf.union(u - 1, v - 1)

        comp_map = defaultdict(list)
        for station in range(c):
            root = uf.find(station)
            comp_map[root].append(station)

        comp_online = {}
        for root, stations in comp_map.items():
            comp_online[root] = SortedSet(stations)

        online = [True] * c 
        results = []

        for qtype, x in queries:
            x -= 1  
            root = uf.find(x)

            if qtype == 1:

                if online[x]:

                    results.append(x + 1)
                else:
                   
                    if comp_online[root]:
                        results.append(comp_online[root][0] + 1)
                    else:
                        results.append(-1)
            else:
                
                if online[x]:
                    online[x] = False
                    comp_online[root].discard(x) 

        return results
