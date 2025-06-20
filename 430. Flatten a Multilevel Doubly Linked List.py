"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        cur = head
        while cur:
            if cur.child:
                h = self.flatten(cur.child)
                tmp = cur.next
                cur.next = h
                h.prev = cur
                while h.next:
                    h = h.next
                h.next = tmp
                if tmp:
                    tmp.prev = h
                cur.child = None
            cur = cur.next
        return head
                