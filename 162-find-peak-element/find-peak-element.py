class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        n = len(nums)
        if len(nums)==1:
            return 0
        while left<right:
            mid = left + (right-left)//2
            if mid==0 and nums[mid]<=nums[mid+1]:
                return mid+1
            elif (nums[mid-1]<nums[mid]>nums[mid+1]) or (mid==0 and nums[mid]>=nums[mid+1]):
                return mid
            elif nums[mid-1]>nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return left