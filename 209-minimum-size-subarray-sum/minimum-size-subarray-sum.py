class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        ans = len(nums)
        s = 0
        left = 0
        for right in range(len(nums)):
            s +=nums[right]
            while s>=target:
                s -=nums[left]
                ans = min(ans,right-left+1)
                left +=1
        return ans
        