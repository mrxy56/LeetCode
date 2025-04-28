# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. Edge case, num3 = 0.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = num3 = 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
            
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
        
        num3 = num1 + num2
        
        if num3 == 0:
            head = ListNode(0)
            return head
        
        head = None
        
        while num3:
            new_node = ListNode(num3 % 10)
            num3 = num3 // 10
            new_node.next = head
            head = new_node
        
        return head
                