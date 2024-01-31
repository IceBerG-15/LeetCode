class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        idx = -1
        for i in range(len(nums)):
            if i==0:
                lsum = 0
                rsum = sum(nums[i+1:])
            elif i==len(nums)-1:
                rsum = 0
                lsum = sum(nums[:i])
            else:
                lsum = sum(nums[:i])
                rsum = sum(nums[i+1:])
            
            if lsum==rsum:
                idx = i
                break
            
        return idx