class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        logval = log10(n)/log10(3)
        return logval==int(logval)