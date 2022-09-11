# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, val):
            if node.val == 1:
                val = val * 2 + 1
            else:
                val = val * 2
            if not node.left and not node.right: # return in the last node, not null
                self.ans += val
                return
            if node.left:
                dfs(node.left, val)
            if node.right:
                dfs(node.right, val)
        dfs(root, 0)
        return self.ans