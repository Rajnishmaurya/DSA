# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj_list=defaultdict(list)

        q=deque()
        q.append(root)

        while q:
            node=q.popleft()

            if node.left:
                adj_list[node.val].append(node.left.val)
                adj_list[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                adj_list[node.val].append(node.right.val)
                adj_list[node.right.val].append(node.val)
                q.append(node.right)

        visited=set()
        q=deque()
        q.append(start)
        visited.add(start)
        answer=0
        while q:
            n=len(q)

            for i in range(n):
                temp=q.popleft()
                for node in adj_list[temp]:
                    if node not in visited:
                        visited.add(node)
                        q.append(node)
            if q:
                answer+=1
        return answer
            


        