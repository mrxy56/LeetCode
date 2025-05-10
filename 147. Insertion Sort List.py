# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while True:
            while cur.next and (cur.val < cur.next.val):
                cur = cur.next
            p = cur.next
            if p is None:
                break
            cur.next = p.next
            prev = None
            ins = head
            while ins and (ins.val < p.val):
                prev = ins
                ins = ins.next
            p.next = ins
            if prev:
                prev.next = p
            else:
                head = p
        return head
            