# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, k): # It is very wise to write a reverse function, making it easier.
            new_head, p = None, head
            while k:
                n = p.next
                p.next = new_head # set a new_head, add node one by one before it.
                new_head = p       
                p = n
                k -= 1
            return new_head
        
        new_head = None
        
        p = head
        ktail = None
        while p:
            count = 0
            p = head
            while count < k and p:
                p = p.next
                count += 1
            if count == k:
                r = reverse(head, k)
                if not new_head:
                    new_head = r
                if ktail:
                    ktail.next = r
                ktail = head
                head = p
        if ktail:
            ktail.next = head
            
        return new_head if new_head else head