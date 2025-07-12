# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        answer=""
        if not root:
            return answer

        q=deque()
        q.append(root)

        while q:
            node=q.popleft()

            if not node:
                answer+="#,"
            else:
                answer+=str(node.val)+','
                q.append(node.left)
                q.append(node.right)
        return answer
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        tokens=data.split(',')

        root_val=int(tokens.pop(0))

        root=TreeNode(root_val)

        q=deque()
        q.append(root)

        while q:
            node=q.popleft()

            left_val=tokens.pop(0)
            if left_val!='#':
                left_node=TreeNode(int(left_val))
                node.left=left_node
                q.append(node.left)
            
            right_val=tokens.pop(0)
            if right_val!='#':
                right_node=TreeNode(int(right_val))
                node.right=right_node
                q.append(node.right)
        return root
            
        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))