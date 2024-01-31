class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        left = 0
        right = n-1
        while left<=right:
            if nums[left]<nums[right]:
                ans = min(ans,nums[left])
                break
            else:
                mid = (left+right)//2
                ans = min(nums[mid],ans)
                if nums[left]<=nums[mid]:
                    left = mid+1
                else:
                    right = mid-1
        return ans