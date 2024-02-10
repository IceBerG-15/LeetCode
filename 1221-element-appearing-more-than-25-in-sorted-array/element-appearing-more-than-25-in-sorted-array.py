class Solution:
    def findSpecialInteger(self, nums: List[int]) -> int:
        d = {}
        avg = len(nums)*(0.25)
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            if d[i]>avg:
                return i
        return -1