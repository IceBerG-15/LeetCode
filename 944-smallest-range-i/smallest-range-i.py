class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        x = max(nums)
        y = min(nums)
        z = x-y-2*k
        if z>0:
            return z
        return 0