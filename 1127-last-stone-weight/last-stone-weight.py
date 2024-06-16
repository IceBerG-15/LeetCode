class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def fun(nums):
            if len(nums)<=1:
                return nums[0]
            nums.sort()
            a = nums.pop()
            b = nums.pop()
            nums.append(abs(a-b))
            return fun(nums)

        return fun(stones)