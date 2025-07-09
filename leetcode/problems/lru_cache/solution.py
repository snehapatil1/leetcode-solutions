class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = defaultdict(ListNode)
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache_map:
            node = self.cache_map[key]
            self.remove(node)
            self.add(node)
            return node.val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            node = self.cache_map[key]
            self.remove(node)
        new_node = ListNode(key, value)
        self.cache_map[key] = new_node
        self.add(new_node)

        if len(self.cache_map) > self.capacity:
            delete_node = self.head.next
            self.remove(delete_node)
            del self.cache_map[delete_node.key]
    
    def add(self, node):
        tail_prev = self.tail.prev
        tail_prev.next = node
        node.prev = tail_prev
        node.next = self.tail
        self.tail.prev = node

    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)