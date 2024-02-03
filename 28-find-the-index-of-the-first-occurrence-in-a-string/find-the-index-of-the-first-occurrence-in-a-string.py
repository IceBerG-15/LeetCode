class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        c = 0
        for i in range(len(haystack)-len(needle)+1):
            j = i+len(needle)
            k = slice(i,j,1)
            if haystack[k]==needle:
                return c
            c +=1
        return -1