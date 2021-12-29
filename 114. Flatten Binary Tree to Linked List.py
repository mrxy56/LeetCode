# Change root in-place, the modifying part is really subtle, you need to think about the tree to do it.
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def flattenTree(self, node):
        if node == None:
            return None
        if node.left == None and node.right == None:
            return node
        leftTail = self.flattenTree(node.left)
        rightTail = self.flattenTree(node.right)
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None
        if rightTail:
            return rightTail
        else:
            return leftTail
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.flattenTree(root)