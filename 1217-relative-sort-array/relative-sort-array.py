class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash1 = {}
        for i in arr1:
            if i not in hash1:
                hash1[i] = 1
            else:
                hash1[i] += 1
        
        ans = []
        for i in arr2:
            ans += [i]*hash1[i]

        arr3 = []
        for i in hash1:
            if i not in arr2:
                arr3 += [i]*hash1[i]
        

        return ans+sorted(arr3)