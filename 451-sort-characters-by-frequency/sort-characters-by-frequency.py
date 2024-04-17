class Solution:
    def frequencySort(self, s: str) -> str:
        hashs = {}
        for i in s:
            if i not in hashs:
                hashs[i] = 1
            else:
                hashs[i] +=1
            
        hashs = dict(sorted(hashs.items(),key = lambda x:x[1]))
        ans = ''
        for i in hashs:
            ans += i*hashs[i]
        return ans[::-1]