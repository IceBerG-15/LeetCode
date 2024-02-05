class MapSum:

    def __init__(self):
        self.dict = {}

    def insert(self, key: str, val: int) -> None:
        self.dict[key] = val

    def sum(self, prefix: str) -> int:
        s = 0
        p = len(prefix)
        for key in self.dict:
            if prefix==key[0:p]:
                s += self.dict[key]
        return s


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)