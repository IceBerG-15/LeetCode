class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = []
        for item in nums:
            n.append(item*item)
        n.sort()  
        return n