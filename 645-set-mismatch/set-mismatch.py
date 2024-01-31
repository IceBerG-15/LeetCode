class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        expected_sum = 0
        for i in range(1,len(nums)+1):
            expected_sum +=i
        unique_sum = sum(set(nums))
        nums_sum = sum(nums)
        return [nums_sum-unique_sum,expected_sum-unique_sum]
        