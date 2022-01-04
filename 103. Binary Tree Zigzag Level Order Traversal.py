# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root == None:
            return []
        from collections import deque
        q = deque()
        q.append(root)
        level = 0
        while(q):
            n = len(q)
            ans.append([])
            for i in range(n):
                node = q.popleft()
                ans[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        for i in range(level):
            if i % 2 == 1:
                ans[i] = reversed(ans[i])
        return ans
        