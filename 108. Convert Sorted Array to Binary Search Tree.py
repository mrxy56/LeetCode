# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l, r):
            if l > r:
                return None
            p = (l + r) // 2
            root = TreeNode(nums[p])
            root.left = dfs(l, p - 1)
            root.right = dfs(p + 1, r)
            return root
        return dfs(0, len(nums) - 1)
    
# This looks hard but keep in mind that preorder and postorder are unique, while inorder has various trees.
# Since it is ascending, it is actually an inorder of a BST.
# All we need to do is to choose the middle one as a root, which means it is heuristically balanced.
# Construct a normal tree.