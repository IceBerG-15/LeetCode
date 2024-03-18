class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = k%n
        if i==0:
            return nums
        for _ in range(i):
            a = nums.pop()
            nums.insert(0,a)
