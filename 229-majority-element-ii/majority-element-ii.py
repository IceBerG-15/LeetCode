class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        d = {}
        n = len(nums)//3
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] +=1
            if d[i]>n and i not in ans:
                ans.append(i)
        return ans