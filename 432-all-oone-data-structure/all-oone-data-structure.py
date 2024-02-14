class AllOne:

    def __init__(self):
        self.all = {}

    def inc(self, key: str) -> None:
        if key in self.all:
            self.all[key]+=1
        else:
            self.all[key]=1

    def dec(self, key: str) -> None:
        self.all[key]-=1
        if self.all[key]==0:
            self.all.pop(key)

    def getMaxKey(self) -> str:
        if len(self.all)<=0:
            return ''
        m = max(self.all.values())
        for i in self.all:
            if self.all[i]==m:
                return i
        return ''

    def getMinKey(self) -> str:
        if len(self.all)<=0:
            return ''
        m = min(self.all.values())
        for i in self.all:
            if self.all[i]==m:
                return i
        return ''


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()