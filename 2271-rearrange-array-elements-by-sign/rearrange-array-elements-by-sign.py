class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        pos = 0
        neg = 1
        for i in nums:
            if i>=0:
                ans[pos] = i
                pos +=2
            else:
                ans[neg] = i
                neg +=2
        return ans