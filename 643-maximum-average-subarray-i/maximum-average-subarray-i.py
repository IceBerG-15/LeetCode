class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        s = max_sum
        for i in range(k,len(nums)):
            s += nums[i]-nums[i-k]
            max_sum = max(s,max_sum)
        return max_sum/k