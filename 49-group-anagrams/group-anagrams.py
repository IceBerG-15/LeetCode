class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for i in strs:
            s = ''.join(sorted(list(i)))
            if s not in hash:
                hash[s] = [i]
            else:
                hash[s].append(i)
        
        ans = []
        for i in hash:
            ans.append(hash[i])
        return ans