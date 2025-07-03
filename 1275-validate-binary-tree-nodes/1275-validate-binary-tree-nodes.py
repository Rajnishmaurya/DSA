class Solution:
    def solve(self,node,adj_list,visit):
        visit[node]=1

        for temp in adj_list[node]:
            if visit[temp]==0:
                self.solve(temp,adj_list,visit)
        return 
        
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        adj_list={}
        in_degree=[0]*n
        for i in range(n):
            adj_list[i]=[]

        for i in range(n):
            if leftChild[i]!=-1:
                adj_list[i].append(leftChild[i])
                in_degree[leftChild[i]]+=1
                if in_degree[leftChild[i]]>1:
                    return False
            if rightChild[i]!=-1:
                adj_list[i].append(rightChild[i])
                in_degree[rightChild[i]]+=1
                if in_degree[rightChild[i]]>1:
                    return False
        
        roots=[i for i in range(n) if in_degree[i]==0]

        if len(roots)!=1:
            return False

        visit=[0]*n
        root=roots[0]
        self.solve(root,adj_list,visit)

        if any(v==0 for v in visit):
            return False


        return True
        # visited=[0]*n

        # dq=deque()
        # dq.append(0)
        # visited[0]=1
        # while dq:
        #     node=dq.popleft()
        #     for temp in adj_list[node]:
        #         if visited[temp]==1:
        #             return False
        #         else:
        #             visited[temp]=1
        #             dq.append(temp)
        # return True


        