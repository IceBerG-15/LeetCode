class Solution:
    def __init__(self):
        self.ans = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(nums, path):
            if len(nums)==0 and path not in self.ans:
                self.ans.append(path)
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:],path+[nums[i]])

        backtrack(nums,[])
        return self.ans