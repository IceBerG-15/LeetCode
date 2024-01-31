class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums)-1
        while begin<=end:
            mid = (begin+end)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                end = mid-1
            else:
                begin = mid+1
        return -1