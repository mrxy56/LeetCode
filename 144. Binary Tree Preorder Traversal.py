# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ret = []
        def dfs(v):
            self.ret.append(v.val)
            if v.left:
                dfs(v.left)
            if v.right:
                dfs(v.right)
        if not root:
            return []
        dfs(root)
        return self.ret