class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = set()
        for i in nums:
            j = abs(i)
            if -j in nums and j in nums:
                ans.add(j)
        if ans:
            return max(list(ans))
        return -1
        