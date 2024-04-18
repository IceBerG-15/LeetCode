class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num%2!=0:
            return False
        
        s = 1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                s+=i+num//i
        return num==s