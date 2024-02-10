class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = list(str(n))
        s = map(int,s)
        prod = 1
        sums = 0
        for i in s:
            prod*=i
            sums+=i
        return prod-sums