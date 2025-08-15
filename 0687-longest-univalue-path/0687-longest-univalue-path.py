# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans=0

        def longestpath(root,value):
            if root:
                left=longestpath(root.left,root.val)
                right=longestpath(root.right,root.val)

                self.ans=max(self.ans, left + right)
                if value==root.val:
                    return max(left,right)+1
            return 0
        
        longestpath(root,None)
        return self.ans