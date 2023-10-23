class RandomizedSet:

    def __init__(self):
        self.map = defaultdict(int)
        self.visited = []

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = len(self.visited)
            self.visited.append(val)
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            last_element = self.visited[-1]
            index_of_element_to_remove = self.map[val]
            
            self.map[last_element] = index_of_element_to_remove
            self.visited[index_of_element_to_remove] = last_element

            self.visited[-1] = val
            
            self.visited.pop()
            self.map.pop(val)
            
            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.visited)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()