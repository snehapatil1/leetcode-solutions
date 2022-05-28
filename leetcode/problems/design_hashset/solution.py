class MyHashSet:

    def __init__(self):
        self.myhashset = set()
        

    def add(self, key: int) -> None:
        self.myhashset.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.myhashset:
            self.myhashset.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.myhashset
        


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.remove(1)
param_3 = obj.contains(1)