# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0 # diameter must be from one leaf to another leaf
        def dfs(node):
            if not node:
                return 0
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            self.diameter = max(self.diameter, left_path + right_path)
            return max(left_path, right_path) + 1
        
        dfs(root)
        return self.diameter