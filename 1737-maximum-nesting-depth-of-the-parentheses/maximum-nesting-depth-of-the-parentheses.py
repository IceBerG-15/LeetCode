class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        counter = 0
        for i in s:
            if i=='(':
                counter +=1
            elif i==')':
                counter -=1
            ans = max(ans,counter)
        return ans