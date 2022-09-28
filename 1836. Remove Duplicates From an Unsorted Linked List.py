# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        h = head
        dummy = ListNode(0)
        dummy.next = head
        d = {}
        while h:
            if d.get(h.val):
                d[h.val] += 1
            else:
                d[h.val] = 1
            h = h.next
        p = dummy.next
        prev = dummy
        while p:
            if d[p.val] > 1:
                prev.next = p.next
            else:
                prev = p # trivial, be careful.
            p = p.next
        return dummy.next
                