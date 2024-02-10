class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        l = sorted(nums)
        if l[-1]>=2*l[-2]:
            return nums.index(l[-1])
        return -1