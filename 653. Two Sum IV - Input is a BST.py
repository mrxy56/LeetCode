# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = []
        def dfs(node):
            if node:
                q.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        d = set()
        for num in q:
            if k - num in d:
                return True
            d.add(num)
        return False