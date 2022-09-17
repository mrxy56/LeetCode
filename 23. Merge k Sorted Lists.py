# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: # Brute Force
        ans = []
        head = p = ListNode(0)
        for l in lists:
            while l:
                ans.append(l.val)
                l = l.next
        for x in sorted(ans):
            p.next = ListNode(x)
            p = p.next
        return head.next