class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1 = {}

        for i in nums1:
            if i not in hash1:
                hash1[i] = 1
            else:
                hash1[i] += 1
        

        ans = []
        for i in nums2:
            if i in hash1:
                ans.append(i)
                hash1[i] -= 1
                if hash1[i]==0:
                    del hash1[i]

        
        return ans