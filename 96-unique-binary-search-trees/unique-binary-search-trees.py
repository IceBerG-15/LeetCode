class Solution:
    def numTrees(self, n: int) -> int:
        res=math.factorial(2*n)//(math.factorial(n)*math.factorial(n+1)) 
        return res