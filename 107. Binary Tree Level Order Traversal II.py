# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        ans = []
        if root is None:
            return []
        q.append((root, 0))
        while q:
            node, dis = q.pop(0)
            if len(ans) <= dis:
                ans.append([])
            ans[dis].append(node.val)
            if node.left:
                q.append((node.left, dis + 1))
            if node.right:
                q.append((node.right, dis + 1))
        return ans[::-1]