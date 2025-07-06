# 1. Should use float('inf') because the treenode value could be 2 ** 31 - 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        minnum = root.val

        def dfs(node):
            if node:
                if node.val > minnum and node.val < self.ans:
                    self.ans = node.val
                else:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        return self.ans if self.ans < float('inf') else -1