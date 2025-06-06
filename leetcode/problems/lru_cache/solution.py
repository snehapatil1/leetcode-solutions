class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.head = None
        self.tail = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
        
        node = ListNode(key, value)
        self.add(node)

        if len(self.dic) > self.capacity:
            delete_node = self.head.next
            self.remove(delete_node)
    
    def add(self, node: ListNode) -> None:
        previousEnd = self.tail.prev
        previousEnd.next = node
        node.prev = previousEnd
        node.next = self.tail
        self.tail.prev = node

        self.dic[node.key] = node

    def remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.dic[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)