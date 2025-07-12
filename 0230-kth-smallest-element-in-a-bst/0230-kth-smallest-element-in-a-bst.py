# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallest(self,root,counter,k,small):
        if not root or counter[0]>=k:
            return 
        self.smallest(root.left,counter,k,small)

        counter[0]+=1

        if counter[0]==k:
            small[0]=root.val
            return 
        self.smallest(root.right,counter,k,small)
        
        
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter=[0]
        small=[float('inf')]
        self.smallest(root,counter,k,small)
        return small[0]
        

        