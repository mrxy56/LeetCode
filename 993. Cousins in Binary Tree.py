# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        p = {root: None}
        seen = {}
        s = [(root, 0)]
        while x not in seen or y not in seen: # Traverse and record parent.
            node, depth = s.pop(0)
            seen[node.val] = (node, depth)
            if node.left:
                p[node.left] = node
                s.append((node.left, depth + 1))
            if node.right:
                p[node.right] = node
                s.append((node.right, depth + 1))
        nodeX, depthX = seen[x]
        nodeY, depthY = seen[y]
        if p[nodeX] == p[nodeY]:
            return False
        else:
            return depthX == depthY