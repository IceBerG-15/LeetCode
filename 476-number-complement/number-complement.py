class Solution:
    def findComplement(self, num: int) -> int:
        n = len(bin(num)[2:])
        a = 2**n-1
        return a^num