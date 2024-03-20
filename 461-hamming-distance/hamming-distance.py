class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        n = len(x)
        m = len(y)
        if n<m:
            x ='0'*(m-n)+x
        elif m<n:
            y = '0'*(n-m)+y
        count = 0
        for i in range(len(x)):
            if x[i]!=y[i]:
                count +=1
        return count