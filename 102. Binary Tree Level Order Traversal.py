# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if root == None:
            return levels
        level = 0
        q = deque([root])
        while q:
            levels.append([])
            level_length = len(q)
            for i in range(level_length):
                node = q.popleft()
                levels[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            level +=1
        return levels