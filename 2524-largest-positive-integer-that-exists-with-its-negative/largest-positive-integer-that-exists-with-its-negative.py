class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        nums = set(nums)
        for num in nums:
            if -num in nums:
                res = max(res, num)
        return res 


        