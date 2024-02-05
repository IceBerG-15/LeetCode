class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        ans = 0
        prod = 1
        for right in range(len(nums)):
            prod *=nums[right]
            if prod>=k:
                while prod>=k and left<=right:
                    prod /=nums[left]
                    left +=1
            ans += right-left+1
        return ans