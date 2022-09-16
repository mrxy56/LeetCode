# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        
        while head and head.next:
            f = head          
            s = head.next
            f.next = s.next
            s.next = f
            p.next = s
            p = f
            head = f.next # Do not use head.next, because head is changed
        return dummy.next