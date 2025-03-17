# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Instead of creating an array, you may build a reversed Linked List.
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p = head
        head2 = None
        while p:
            tmp = ListNode(p.val)
            tmp.next = head2
            head2 = tmp
            p = p.next
        p = head
        ans = 0
        while head and head2:
            if head.val + head2.val > ans:
                ans = head.val + head2.val
            head = head.next
            head2 = head2.next
        return ans
        
            