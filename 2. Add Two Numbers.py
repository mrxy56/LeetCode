# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        h = ListNode(0)
        cur = h
        while l1 or l2 or c > 0:
            v1 = l1.val if l1 else 0   # This grammar is useful, a good practice of linked list, needs to review in the future
            v2 = l2.val if l2 else 0
            s = v1 + v2 + c
            c = s // 10
            node = ListNode(s % 10)
            cur.next = node
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return h.next