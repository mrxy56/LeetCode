# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. Pay attention to details. Node values can be negative.
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, cur):
            if node is None:
                return
            if cur <= node.val:
                self.ans += 1
                cur = node.val
            if node.left:
                dfs(node.left, cur)
            if node.right:
                dfs(node.right, cur)
        dfs(root, root.val)
        return self.ans