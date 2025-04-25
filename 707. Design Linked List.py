# 1. Pay attention to the edge cases.
# 2. For add at head or tail, consider length is 1.
# 3. For delete or get, consider index is too big or is 0.
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        if index >= self.len:
            return -1
        p = self.head
        for i in range(index):
            p = p.next
        return p.val

    def addAtHead(self, val: int) -> None:
        if self.len == 0:
            self.head = ListNode(val)
            self.len += 1
        else:
            newNode = ListNode(val)
            newNode.next = self.head
            self.head = newNode
            self.len += 1

    def addAtTail(self, val: int) -> None:
        if self.len == 0:
            self.head = ListNode(val)
            self.len += 1
        else:
            p = self.head
            for i in range(self.len - 1):
                p = p.next
            p.next = ListNode(val)
            self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.len:
            return -1
        if index == 0:
            self.addAtHead(val)
        else:
            p = self.head
            for i in range(index - 1):
                p = p.next
            newNode = ListNode(val)
            newNode.next = p.next
            p.next = newNode
            self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return -1
        if index == 0:
            self.head = self.head.next
            self.len -= 1
        else:
            p = self.head
            for i in range(index - 1):
                p = p.next
            p.next = p.next.next
            self.len -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)