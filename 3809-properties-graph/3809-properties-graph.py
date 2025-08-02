class Solution:
    def __init__(self):
        self.parent=[]
        self.rank=[]
    
    def find(self, x):
        if x==self.parent[x]:
            return x
        else:
            return self.find(self.parent[x])
    
    def union(self, a, b):
        root_x=self.find(a)
        root_y=self.find(b)

        if root_x!=root_y:
            if self.rank[root_x]>self.rank[root_y]:
                self.parent[root_y]=root_x
            elif self.rank[root_x]<self.rank[root_y]:
                self.parent[root_x]=root_y
            else:
                self.parent[root_y]=root_x
                self.rank[root_x]+=1
    def intersect(self,k,list1,list2):
        count1=Counter(list1)
        count2=Counter(list2)

        common_count=sum(1 for item in count1 if item in count2)
        return common_count>=k

    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        m=len(properties)
        self.parent=list(range(m))
        self.rank=[0]*m

        for i in range(m):
            for j in range(i+1,m):
                if self.intersect(k,properties[i],properties[j]):
                    self.union(i,j)
        
        return sum(1 for i in range(m) if self.find(i)==i)


        