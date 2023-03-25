class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        keys = self.cache.keys()
        if key in keys:
            self.cache[key] = value
            self.queue.remove(key)
            self.queue.append(key)
        else:
            if len(keys) >= self.capacity:
                del self.cache[self.queue[0]]
                self.queue.pop(0)
            self.cache.update({key : value})
            self.queue.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)