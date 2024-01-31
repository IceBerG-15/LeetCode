class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numsList = nums
        self.kth = k

    def add(self, val: int) -> int:
        self.numsList.append(val)
        self.numsList.sort()
        return self.numsList[-self.kth]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)