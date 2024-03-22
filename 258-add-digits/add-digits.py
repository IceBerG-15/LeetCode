class Solution:
    def addDigits(self, num: int) -> int:
        def func(n):
            if 0<=n<=9:
                return n
            s = 0
            while n>0:
                r = n%10
                s +=r
                n //=10
            return func(s)
        
        return func(num)
