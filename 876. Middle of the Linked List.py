# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Please pay attention that if we want tmp to start from 0, the initial value should be -1.
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        p = head
        tmp = -1
        while p:
            tmp += 1
            if tmp == (n // 2):
                return p
            p = p.next