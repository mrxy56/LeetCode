"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# It is very wise to save leftmost, previous node. And update them one by one. Deal with it layer by layer.
class Solution:
    def processChild(self, childNode, prev, leftmost):
        if childNode:
            if prev:
                prev.next = childNode
            else:
                leftmost = childNode
            prev = childNode
        return prev, leftmost
    
    def connect(self, root: 'Node') -> 'Node':    
        if root == None:
            return root
        leftmost = root
        while leftmost:
            prev, curr = None, leftmost
            leftmost = None
            while curr:
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                curr = curr.next
        return root