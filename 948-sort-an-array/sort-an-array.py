class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ans = []
        heapify(nums)
        for _ in range(len(nums)):
            ans.append(heappop(nums))
        
        return ans