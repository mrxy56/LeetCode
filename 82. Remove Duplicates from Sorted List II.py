# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        p = head
        while p:
            if p.next and p.next.val == p.val:
                while p.next and p.next.val == p.val:
                    p.next = p.next.next
                prev.next = p.next
                p = prev.next
            else:
                prev = p
                p = p.next
        return dummy.next