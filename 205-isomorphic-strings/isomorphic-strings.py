class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        hashs = {}
        mapped = set()
        for i in range(len(s)):
            if s[i] not in hashs and t[i] not in mapped:
                hashs[s[i]] = t[i]
                mapped.add(t[i])
            else:
                if s[i] not in hashs or hashs[s[i]]!=t[i]:
                    return False
        return True