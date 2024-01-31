class Solution:
    def reverseBits(self, n: int) -> int:
        bin = ''
        while n>0:
            bin = bin+str(n%2)
            n = n//2
        if len(bin)<32:
            j = 32-len(bin)
            bin = bin+'0'*j
        k = -1
        sum = 0
        for i in bin[::-1]:
            k = k+1
            if i=='1':
                sum = sum+2**k
        return sum
