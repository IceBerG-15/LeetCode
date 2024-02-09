class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        ans = []
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                ans.append(i)
        return ans