class Solution:
    def __init__(self):
        self.ans = []

    def backtrack(self, nums, path):
        if len(nums)==0 and path not in self.ans:
            self.ans.append(path)
        for i in range(len(nums)):
            self.backtrack(nums[:i]+nums[i+1:],path+[nums[i]])

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums,[])
        return self.ans