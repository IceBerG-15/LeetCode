class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        i = 0
        while i<len(nums):
            count = 0
            if nums[i]==1:
                right = i
                while right<len(nums) and nums[right]==1:
                    right +=1
                    count +=1
                m = max(m,count)
                i = right
            i+=1
        return m

        