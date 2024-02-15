class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        left = 0
        while left<len(nums):
            if nums[left]==1:
                right = left
                while right<len(nums) and nums[right]==1:
                    right +=1
                m = max(m,right-left)
                left = right
            left+=1
        return m

        