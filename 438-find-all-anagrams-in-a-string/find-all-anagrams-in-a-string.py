class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = ''.join(sorted(list(p)))
        def check(a):
            a = ''.join(sorted(list(a)))
            if a==p:
                return True
            return False
        
        l = len(p)
        left = 0
        ans = []
        for right in range(l,len(s)+1):
            if check(s[left:right]):
                ans.append(left)
            left +=1
        return ans