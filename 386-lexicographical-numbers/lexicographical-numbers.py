class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l = [str(x) for x in range(1,n+1)]
        return list(map(int,sorted(l)))
        