class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        count = {}
        ans = 0
        right = 0
        left = 0
        while right<len(nums):
            i = nums[right]
            if i not in count:
                count[i] = 1
            else:
                count[i] +=1
                while count[i]>k:
                    count[nums[left]]-=1
                    left +=1
            ans = max(ans,right-left+1)
            right +=1
        return ans
