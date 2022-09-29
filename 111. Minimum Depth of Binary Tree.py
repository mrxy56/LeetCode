# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = []
        if root == None: # root can be None
            return 0
        q.append((root, 1))
        while q:
            node, d = q.pop(0)
            if not node.left and not node.right:
                return d
            else:
                if node.left:
                    q.append((node.left, d + 1))
                if node.right:
                    q.append((node.right, d + 1))