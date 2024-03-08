class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0]*101
        max_freq = 0
        for i in nums:
            freq[i] += 1
            max_freq = max(max_freq,freq[i])
        count = 0
        for i in freq:
            if i==max_freq:
                count +=i
        return count