class MyNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if (not self.head):
            return -1
        if index < 0 or index >= self.size:
            return -1
        n = self.head
        for i in range(index):
            n = n.next
        if n:
            return n.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = MyNode(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:     
        if (not self.head):
            self.addAtHead(val)
            return
        n = self.head
        while n.next:
            n = n.next
        n.next = MyNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            n = self.head
            for i in range(index-1):
                n = n.next
            node = MyNode(val)
            node.next = n.next
            n.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        n = self.head
        if index == 0:
            self.head = n.next
        else:
            for i in range(index-1):
                n = n.next
            if n and n.next and n.next.next:
                n.next = n.next.next
            else:
                n.next = None
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)