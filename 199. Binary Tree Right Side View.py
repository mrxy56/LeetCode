# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. Very subtle to use depth to control whether to append it to ans.
# 2. Use search order to satify the priority condition.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ls = []
        def dfs(node, depth):
            if not node:
                return
            if len(self.ls) == depth:
                self.ls.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return self.ls