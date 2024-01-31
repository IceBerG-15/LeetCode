class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat=[]
        for i in pattern:
            pat.append(i)
        st = s.split(" ")
        if len(pat)!=len(st):
            return False
        if len(set(pat))!=len(set(st)):
            return False
        d = {}
        for i in range(len(pat)):
            if st[i] not in d:
                d[st[i]] = pat[i]
            elif d[st[i]]!=pat[i]:
                return False
        return True