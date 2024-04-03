class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hashmap = {}
        for i in s1.split(' ')+s2.split(' '):
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] +=1
        
        ans = []
        for i in hashmap:
            if hashmap[i]==1:
                ans.append(i)
        return ans