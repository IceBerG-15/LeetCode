class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l = [str(x) for x in range(1,n+1)]
        l = sorted(l)
        l = list(map(int,l))
        return l
        