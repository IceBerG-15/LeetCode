class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        c = 0
        ans = 0
        for i in columnTitle[::-1]:
            ans += (ord(i)-64)*(26**c)
            c +=1
        return ans