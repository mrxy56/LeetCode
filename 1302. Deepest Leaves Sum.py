# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1. Traverse + arrange the nodes to the right place.
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        ls = []
        def dfs(node, depth):
            if len(ls) == depth:
                ls.append([])
            ls[depth].append(node.val)
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
        dfs(root, 0)
        return sum(ls[-1])