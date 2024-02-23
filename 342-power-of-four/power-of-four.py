class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        logval = log10(n)/log10(4)
        if logval==int(logval):
            return True
        return False