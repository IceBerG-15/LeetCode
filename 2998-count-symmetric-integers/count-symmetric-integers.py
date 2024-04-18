class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low,high+1):
            m = str(i)
            if len(m)%2==0:
                a = int(m[:len(m)//2])
                b = int(m[len(m)//2:])
                s1,s2 = 0,0
                while a:
                    s1 +=a%10
                    a = a//10
                while b:
                    s2 +=b%10
                    b = b//10
                if s1==s2:
                    count +=1
        return count