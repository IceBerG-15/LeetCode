class Solution:
    def romanToInt(self, s: str) -> int:
        b=0
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        for i in range(len(s)):
            a=s[i]
            if a=='I':
                b+=1
            elif a=='V':
                b+=5
            elif a=='X':
                b+=10
            elif a=='L':
                b+=50
            elif a=='C':
                b+=100
            elif a=='D':
                b+=500
            else:
                b+=1000
        return b