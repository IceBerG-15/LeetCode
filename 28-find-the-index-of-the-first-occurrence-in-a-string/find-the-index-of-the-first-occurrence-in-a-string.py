class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        c = 0
        for i in range(len(haystack)-len(needle)+1):
            j = i+len(needle)
            if haystack[slice(i,j)]==needle:
                return c
            c +=1
        return -1