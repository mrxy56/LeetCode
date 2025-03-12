# 1. Use the self.ans as a global variable.
# 2. Take care of the node is None case.
# 3. Be careful about the logic.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, dir, depth):
            if node is None:
                return
            if depth + 1 > self.ans:
                self.ans = depth + 1
            if dir == 'L':
                if node.right:
                    dfs(node.right, 'R', depth + 1)
                if node.left:
                    dfs(node.left, 'L', 0)
            if dir == 'R':
                if node.left:
                    dfs(node.left, 'L', depth + 1)
                if node.right:
                    dfs(node.right, 'R', 0)
        if root.left:
            dfs(root.left, 'L', 0)
        if root.right:
            dfs(root.right, 'R', 0)
        return self.ans