class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        maxI , minI , badI = -1,-1,-1
        ans = 0
        for i, num in enumerate(nums):
            if not minK<=num<=maxK:
                badI = i
            if num==minK:
                minI = i
            if num==maxK:
                maxI = i
            smaller = min(minI,maxI)
            temp = smaller-badI
            ans += temp if temp>0 else 0
        return ans