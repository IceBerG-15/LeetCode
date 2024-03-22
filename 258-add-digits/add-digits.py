class Solution:
    def addDigits(self, num: int) -> int:
        def func(n):
            if 0<=n<=9:
                return n
            l = list(map(int,list(str(n))))
            return func(sum(l))
        
        return func(num)
