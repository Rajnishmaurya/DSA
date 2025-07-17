class Solution:
    def dfs(self,airport):
        while self.adj_list[airport]:
            temp=self.adj_list[airport].pop()
            self.dfs(temp)
        self.route.append(airport)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.route=[]
        self.adj_list=defaultdict(list)

        for x,y in tickets:
            self.adj_list[x].append(y)
        
        for key in self.adj_list:
            self.adj_list[key]=sorted(self.adj_list[key],reverse=True)
        
        self.dfs("JFK")
        return self.route[::-1]

        #Eulerpath
        