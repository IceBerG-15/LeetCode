class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        count = 0
        for i in s[::-1]:
            if i=='1':
                num += 2**count
            count += 1
        
        ans = 0
        while num!=1:
            if num%2==0:
                num = num//2
            else:
                num = num+1
            ans += 1


        return ans