from math import factorial as fac
class Solution:
    def numTrees(self, n: int) -> int:
        res=fac(2*n)//(fac(n)*fac(n+1)) 
        return res