# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(node, path):
            new_path = path + '->' + str(node.val)
            if node is None:
                return
            if node.left is None and node.right is None:
                ans.append(new_path)
            if node.left:
                dfs(node.left, new_path)
            if node.right:
                dfs(node.right, new_path)
                
        if not root.left and not root.right:
            return [str(root.val)]

        if root.left:
            dfs(root.left, str(root.val))
        if root.right:
            dfs(root.right, str(root.val))
        return ans