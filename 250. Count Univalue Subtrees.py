# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. Identify if each node is a root of a univalue subtree.
# 2. Four circumstances depending on if the subtree is None.
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if node is None:
                return True
            if node.left is None and node.right is None:
                self.ans += 1
                return True
            flag1 = dfs(node.left)
            flag2 = dfs(node.right)
            if node.left and not node.right and flag1 and node.val == node.left.val:
                self.ans += 1
                return True
            elif node.right and not node.left and flag2 and node.val == node.right.val:
                self.ans += 1
                return True
            elif node.left and node.right and flag1 and flag2:
                if node.left.val == node.right.val and node.left.val == node.val:
                    self.ans += 1
                    return True
        dfs(root)
        return self.ans
        