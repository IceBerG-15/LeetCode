class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash = {}
        ans = 0
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        for i in nums:
            hash[i] -=1
            ans += hash[i]
        return ans