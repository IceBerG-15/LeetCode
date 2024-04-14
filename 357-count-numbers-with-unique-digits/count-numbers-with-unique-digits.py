import math
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
        def count(n,ans):
            if n==0:
                return int(ans+1)
            ans += 9*math.factorial(9)//math.factorial(10-n)
            print(ans)
            return count(n-1,ans)
        return count(n,0)