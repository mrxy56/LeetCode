# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findleaf(node, ls):
            if node.left is None and node.right is None:
                ls.append(node.val)
                return
            if node.left:
                findleaf(node.left, ls)
            if node.right:
                findleaf(node.right, ls)
        ls1 = []
        ls2 = []
        findleaf(root1, ls1)
        findleaf(root2, ls2)
        if len(ls1) != len(ls2):
            return False
        n = len(ls1)
        i = 0
        while i < n:
            if ls1[i] != ls2[i]:
                return False
            i += 1
        return True