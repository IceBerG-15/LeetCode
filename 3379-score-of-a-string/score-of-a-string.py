class Solution:
    def scoreOfString(self, s: str) -> int:
        asc = []
        for i in s:
            asc.append(ord(i))
        left = 0
        right = 1
        if len(asc)==0:
            return asc[0]
        ans = 0
        while right<len(asc):
            ans += abs(asc[left]-asc[right])
            left +=1
            right+=1
        return ans