class RandomizedSet:

    def __init__(self):
        self.hmap = defaultdict(int)
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False
        self.arr.append(val)
        self.hmap[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.hmap:
            last_val, val_idx = self.arr[-1], self.hmap[val]
            self.arr[val_idx], self.hmap[last_val] = last_val, val_idx
            self.arr.pop()
            del self.hmap[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()