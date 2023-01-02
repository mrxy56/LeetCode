# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1. Must do a series of returns in the recursion.
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(v):
            if not v or v.val == val:
                return v
            if val < v.val:
                return dfs(v.left)
            else:
                return dfs(v.right)
        return dfs(root)