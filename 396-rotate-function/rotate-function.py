class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s = 0
        original = 0
        for i,val in enumerate(nums):
            s += val
            original += i*val
        m = original
        n = len(nums)
        for i in range(n-1,0,-1):
            original += s-nums[i]*n
            m = max(m,original)
        return m