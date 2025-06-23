# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        def dfs(node):
            self.cnt += 1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        if not root:
            return 0
        dfs(root)
        return self.cnt