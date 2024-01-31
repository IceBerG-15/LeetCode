class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i]=1
            d[i] = d[i]+1
        for i in d.keys():
            if d[i]==max(d.values()):
                return i
        return -1