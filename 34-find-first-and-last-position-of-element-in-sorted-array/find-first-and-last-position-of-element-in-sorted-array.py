class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(nums,target,isFirst):
            n = len(nums)
            left = 0
            right = n - 1
            ans = -1
            while left<=right:
                mid = (left+right)//2
                if target<nums[mid]:
                    right = mid-1
                elif target>nums[mid]:
                    left = mid+1
                else:
                    ans = mid
                    if isFirst:
                        right = mid-1
                    else:
                        left = mid+1
            return ans
        
        first = binarySearch(nums,target,True)
        last = binarySearch(nums,target,False)
        return [first,last]