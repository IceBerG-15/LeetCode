class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        l=[]
        for i in t:
            l.append(i)
        for i in s:
            if i not in l:
                return False
            l.remove(i)
        return True