# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        p = dummy
        q = dummy
        cnt1 = cnt2 = 0
        while p:
            cnt1 += 1
            p = p.next
            q = q.next
            if cnt1 == m and p:
                while q:
                    cnt2 += 1
                    q = q.next
                    if cnt2 == n or not q:
                        break
                if q:
                    p.next = q.next
                else:
                    p.next = None
                p = q
                cnt1 = cnt2 = 0
        return dummy.next