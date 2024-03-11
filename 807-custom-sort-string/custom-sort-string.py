class Solution:
    def customSortString(self, order: str, s: str) -> str:
        diff = ''
        hash = {}
        for i in s:
            if i not in order:
                diff +=i
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        ans = ''
        for i in order:
            if i in hash:
                ans += i*hash[i]
        return ans+diff
                