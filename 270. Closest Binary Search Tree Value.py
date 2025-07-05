# 1. A little bit hard to think. Firstly consider diff, then smallest.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        mindiff = 2 ** 31 - 1
        ans = []
        while root:
            if abs(root.val - target) <= mindiff:
                mindiff = abs(root.val - target)
                ans.append((mindiff, root.val))
            if target < root.val:
                root = root.left
            else:
                root = root.right
        ans.sort(key=lambda x: (x[0], x[1]))
        return ans[0][1]