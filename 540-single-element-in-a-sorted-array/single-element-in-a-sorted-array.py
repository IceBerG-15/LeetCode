class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        left = 0
        for right in range(1,len(nums),2):
            if nums[left]^nums[right]!=0:
                return nums[left]
            left +=2
        return nums[left]