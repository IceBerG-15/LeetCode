class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        ans = []
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]>1:
                ans.append(i)
        return ans 
        