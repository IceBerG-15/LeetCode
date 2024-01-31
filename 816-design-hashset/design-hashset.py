class MyHashSet:

    def __init__(self):
        self.hash = {}

    def add(self, key: int) -> None:
        self.hash[key] = True

    def remove(self, key: int) -> None:
        self.hash[key] = False

    def contains(self, key: int) -> bool:
        if key in self.hash:
            return self.hash[key]
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)