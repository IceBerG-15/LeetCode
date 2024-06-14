class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        numTracker = 0
        minIncreament = 0

        for i in nums:
            numTracker = max(numTracker, i)
            minIncreament += numTracker - i
            numTracker += 1
        return minIncreament