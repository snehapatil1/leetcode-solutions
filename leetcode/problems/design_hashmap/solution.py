class MyHashMap:

    def __init__(self):
        self.myhashmap = {}
        

    def put(self, key: int, value: int) -> None:
        self.myhashmap.update({key : value})

    def get(self, key: int) -> int:
        if key in self.myhashmap.keys():
            return self.myhashmap[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self.myhashmap.keys():
            self.myhashmap.pop(key)


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,10)
param_2 = obj.get(1)
obj.remove(1)