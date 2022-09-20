# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head
        cnt = 0
        if k == 0: # several edge cases
            return head
        if not head or not head.next:
            return head
        while p:
            p = p.next
            cnt += 1
        p = head
        for i in range(cnt - k % cnt - 1): # k % cnt, not k
            p = p.next
        tail = p
        if not p.next: # This is a special case, what if we do not need to rotate?
            return head
        new_head = p.next
        for i in range(k % cnt):
            p = p.next
        p.next = head
        tail.next = None
        return new_head