class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x^y)[2:]
        count = 0
        for i in range(len(a)):
            if a[i]=='1':
                count +=1
        return count