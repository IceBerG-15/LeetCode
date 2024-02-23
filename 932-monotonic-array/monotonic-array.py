class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def increase(nums):
            left = 0
            while left+1<len(nums):
                right = left+1
                if nums[left]>nums[right]:
                    return False
                left +=1
            return True
        
        def decrease(nums):
            left = 0
            while left+1<len(nums):
                right = left+1
                if nums[left]<nums[right]:
                    return False
                left +=1
            return True
        
        return increase(nums) or decrease(nums)