class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        if n==0:
            return True
        i = 0
        for j in t:  
            if j==s[i]:
                i+=1 
                if i==n:
                    break
        if i==n:
            return True
        return False