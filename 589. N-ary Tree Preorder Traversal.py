"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 1. Use stack to do the traversal, worth memorizing.
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]  
        ans = []       
        while stack:
            v = stack.pop()
            ans.append(v.val)
            stack = stack + v.children[::-1]
        return ans