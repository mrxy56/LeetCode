# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ret = []
        def dfs(v):
            if v.left:
                dfs(v.left)
            if v.right:
                dfs(v.right)
            self.ret.append(v.val)
        if not root:
            return []
        dfs(root)
        return self.ret