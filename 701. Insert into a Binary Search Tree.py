# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1. Make sure the direction is correct.
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(pa, v, dir):
            if not v:
                if dir == 'l':
                    pa.left = TreeNode(val)
                elif dir == 'r':
                    pa.right = TreeNode(val)
                return
            if v.val < val:
                dfs(v, v.right, 'r')
            else:
                dfs(v, v.left, 'l')
        if not root:
            return TreeNode(val)
        dfs(None, root, 'm')
        return root