class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            j = abs(i)
            if j not in ans and -j in nums and j in nums:
                ans.append(j)
        if ans:
            return max(ans)
        return -1
        