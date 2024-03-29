class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        m = max(nums)
        count = 0
        left = 0
        right = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right]==m:
                count +=1
            while count>=k:
                if nums[left]==m:
                    count -=1
                left +=1
            ans +=left
        return ans
        