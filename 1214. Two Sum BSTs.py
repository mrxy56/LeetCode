# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        l1 = []
        l2 = []
        def dfs(root, l):
            l.append(root.val)
            if root.left:
                dfs(root.left, l)
            if root.right:
                dfs(root.right, l)
        dfs(root1, l1)
        dfs(root2, l2)
        s2 = set(l2)
        for r in l1:
            if target - r in s2:
                return True
        return False
        