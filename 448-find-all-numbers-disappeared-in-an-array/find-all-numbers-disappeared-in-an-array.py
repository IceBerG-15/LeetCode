class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = []
        n = set(nums)
        for i in range(1,len(nums)+1):
            if i not in n:
                l.append(i)
        return l