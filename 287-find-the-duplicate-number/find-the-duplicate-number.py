class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = set()
        for i in nums:
            if i in l:
                return i
            l.add(i)
        