class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        t = n//5
        while t>0:
            ans +=t
            t = t//5
        return ans