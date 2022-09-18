# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0) # dummy is the key
        dummy.next = head
        i = dummy
        l = 0
        while i:
            l += 1
            i = i.next
        k = l - n - 1
        j = dummy
        while k > 0:
            j = j.next
            k -= 1
        t = j
        t.next = j.next.next
        return dummy.next
            