# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. Use p to cut the string, instead of searching for the specific element. Because you don't know if it is None.
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(inorder, postorder):
            n1 = len(inorder)
            n2 = len(postorder)
            if n1 == 0 or n2 == 0:
                return None
            node = TreeNode(postorder[n2 - 1])
            p = 0
            while p < n1 and inorder[p] != postorder[n2 - 1]:
                p += 1
            node.left = dfs(inorder[:p], postorder[:p])
            node.right = dfs(inorder[p + 1:], postorder[p:n2 - 1])
            return node
        
        root = dfs(inorder, postorder)
        return root