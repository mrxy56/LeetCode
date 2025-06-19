"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def postorder(node):
            if node.left is None and node.right is None:
                return node, node
            lh = None
            lt = None
            rh = None
            rt = None
            if node.left:
                lh, lt = postorder(node.left)
                head = lh
            else:
                head = node
            if node.right:
                rh, rt = postorder(node.right)
                tail = rt
            else:
                tail = node
            node.left = lt
            if lt:
                lt.right = node
            node.right = rh
            if rh:
                rh.left = node
            return head, tail
        if root is None:
            return None
        head, tail = postorder(root)
        head.left = tail
        tail.right = head
        return head