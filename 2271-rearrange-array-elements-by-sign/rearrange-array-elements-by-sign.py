class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for i in nums:
            if i<0:
                negatives.append(i)
            else:
                positives.append(i)
        k = 1
        for i in negatives:
            positives.insert(k,i)
            k+=2
        return positives