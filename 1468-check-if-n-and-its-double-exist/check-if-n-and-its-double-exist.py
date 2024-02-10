class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i,val in enumerate(arr):
            val = val*2
            if val in arr and arr.index(val)!=i:
                return True
        return False