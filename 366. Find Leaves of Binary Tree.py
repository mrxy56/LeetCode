# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def dfs(node):
            if not node:
                return -1
            lh = dfs(node.left)
            rh = dfs(node.right)
            h = max(lh, rh) + 1 # definition of height
            if len(ans) == h:
                ans.append([])
            ans[h].append(node.val)
            return h
        dfs(root)
        return ans