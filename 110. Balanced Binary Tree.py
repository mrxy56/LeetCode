# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.n = 0
        self.d = 0
        def dfs(node, depth):
            if node is None:
                return (True, 0)
            flag_l, ld = dfs(node.left, depth + 1)
            flag_r, rd = dfs(node.right, depth + 1)
            ret = abs(ld - rd) <= 1 and flag_l and flag_r
            d = max(ld, rd) + 1
            return ret, d
                
        flag, d = dfs(root, 0)
        return flag
        