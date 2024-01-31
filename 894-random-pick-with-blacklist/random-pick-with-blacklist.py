from random import randint
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        val = n-len(blacklist)-1
        self.hash = {}
        for b in blacklist:
            if b<=val:
                while n-1 in blacklist:
                    n -=1
                self.hash[b] = n-1
                n -=1
        self.n = val+1

    def pick(self) -> int:
        idx = randint(0,self.n-1)
        return self.hash.get(idx,idx)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()