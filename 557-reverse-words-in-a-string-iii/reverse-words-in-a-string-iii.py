class Solution:

    def reverseWords(self, s: str) -> str:
        def rev(s:str)->str:
            return s[::-1]

        s = s.split(' ')
        s = list(map(rev,s))
        return ' '.join(s)