# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. Binary search tree's inorder is determined so only consider preorder or postorder.
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        pre_order = []
        in_order = []
        def preorder(node):
            if node is None:
                return
            pre_order.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
            
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            in_order.append(str(node.val))
            inorder(node.right)
        
        preorder(root)
        inorder(root)
        return '.'.join(pre_order) + '+' + '.'.join(in_order)
            
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if data == '+':
            return None
        pre_order, in_order = data.split('+')
        pre_order = pre_order.split('.')
        in_order = in_order.split('.')
        def dfs(pre_order, in_order):
            if len(pre_order) == 0:
                return None
            if len(pre_order) == 1:
                return TreeNode(int(pre_order[0]))
            node = TreeNode(int(pre_order[0]))
            n = len(in_order)
            for i in range(n):
                if in_order[i] == pre_order[0]:
                    node.left = dfs(pre_order[1:i + 1], in_order[:i])
                    node.right = dfs(pre_order[i + 1:], in_order[i + 1:])
            return node
        root = dfs(pre_order, in_order)
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans