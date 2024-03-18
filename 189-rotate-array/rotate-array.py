class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = k%n
        if i==0:
            return nums
        a = nums[-i:]
        for i in a[::-1]:
            nums.pop()
            nums.insert(0,i)
