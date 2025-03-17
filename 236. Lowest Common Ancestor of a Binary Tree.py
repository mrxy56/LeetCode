# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. It is better to use a dictionary to record the parent pointer to do backtracking.
# 2. You may also use a stack to track the candidate ancestor once visiting p or q.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.q1 = []
        self.q2 = []
        def dfs(node, fa, target, q, mode):
            q.append(node)
            if node.val == target.val:
                if mode == 1:
                    self.q1 = deepcopy(q)
                else:
                    self.q2 = deepcopy(q)
                return
            if node.left:
                dfs(node.left, node, target, q, mode)
            if node.right:
                dfs(node.right, node, target, q, mode)
            q.pop()
        dfs(root, root, p, [], 1)
        dfs(root, root, q, [], 2)
        len1 = len(self.q1)
        len2 = len(self.q2)
        i = j = 0
        while i < len1 and j < len2 and self.q1[i].val == self.q2[j].val:
            i += 1
            j += 1
        return self.q1[i - 1]