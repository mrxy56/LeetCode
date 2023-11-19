# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        if cnt == 1:
            return None
        mid = cnt // 2
        p = dummy
        for i in range(mid):
            p = p.next
        p.next = p.next.next
        return dummy.next