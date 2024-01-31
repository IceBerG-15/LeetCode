class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        idx = -1
        s = sum(nums)
        for i in range(len(nums)):
            if i==0:
                lsum = 0
                rsum = s-nums[i]
            elif i==len(nums)-1:
                rsum = 0
                lsum = s-nums[i]
            else:
                lsum = sum(nums[:i])
                rsum = sum(nums[i+1:])
            
            if lsum==rsum:
                idx = i
                break
            
        return idx
            