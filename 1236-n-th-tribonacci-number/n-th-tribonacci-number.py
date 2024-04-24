class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        
        if n==0:
            return a
        elif n==1:
            return b
        elif n==2:
            return c
        else:
            for _ in range(n-2):
                d = a+b+c
                a = b
                b = c
                c = d
            return d
