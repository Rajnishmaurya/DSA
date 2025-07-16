# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,count,target,hash_map,total):
        if not root:
            return
        total+=root.val
        if target==total:
            count[0]+=1
        
        if hash_map[total-target]:
            count[0]+=hash_map[total-target]
        hash_map[total]+=1
        self.solve(root.left,count,target,hash_map,total)
        self.solve(root.right,count,target,hash_map,total)
        hash_map[total]-=1

        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count=[0]
        hash_map=defaultdict(int)
        total=0
        self.solve(root,count,targetSum,hash_map,total)
        return count[0]
        