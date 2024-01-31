class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=''
        s = s.lower()
        for i in s:
            if (i>='a' and i<='z') or (i>='0' and i<='9'):
                string = string+i
        if string==string[::-1]:
            return True
        return False