class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        nums = nums[::-1]
        m1 = nums[0]*nums[1]*nums[2]
        m2 = nums[0]*nums[-1]*nums[-2]
        if m1>m2:
            return m1
        return m2