# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 1. Properties of BST:
# (1) Left subtree of a node N contains nodes whose values are lesser than or equal to node N's value.
# (2) Right subtree of a node N contains nodes whose values are greater than node N's value.
# (3) Both left and right subtrees are also BSTs.
#
# BST Algorithm
# (1) Start traversing the tree from the root node.
# (2) If both the nodes p and q are in the right subtree, then continue the search with right subtree starting step 1.
# (3) If both the nodes p and q are in the left subtree, then continue the search with left subtree starting step 1.
# (4) If both step 2 and step 3 are not true, this means we have found the node which is common to node p's and q's subtrees. and hence we return this common node as the LCA.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(v, p, q):
            if p == v.val or q == v.val:
                return v
            if p <= v.val and q <= v.val:
                return dfs(v.left, p, q)
            elif p > v.val and q > v.val:
                return dfs(v.right, p, q)
            else:
                return v
        if not p:
            return q
        if not q:
            return p
        return dfs(root, p.val, q.val)