"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            node = Node(insertVal)
            node.next = node
            head = node
            return head
        if head.next is head:
            node = Node(insertVal)
            head.next = node
            node.next = head
            return head
        cur = head
        cnt = 0
        while cur:
            if insertVal >= cur.val and insertVal <= cur.next.val:
                node = Node(insertVal)
                node.next = cur.next
                cur.next = node
                break
            cur = cur.next
            if cur.next == head:
                cnt += 1
            if cnt >= 2:
                while cur:
                    if cur.val > cur.next.val:
                        node = Node(insertVal)
                        node.next = cur.next
                        cur.next = node
                        return head
                    cur = cur.next
                    if cur.next == head:
                        cnt += 1
                    if cnt == 3:
                        node = Node(insertVal)
                        node.next = cur.next
                        cur.next = node
                        return head
        return head