class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        i = 0
        for j in t:
            if i==len(s):
                return True
            if j==s[i]:
                i+=1 
        if i==len(s):
                return True
        return False