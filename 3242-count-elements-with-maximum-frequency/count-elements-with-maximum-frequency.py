class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] +=1
        m = max(hash.values())
        count = 0
        for i in hash:
            if hash[i]==m:
                count +=hash[i]
        return count