class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1 = {}
        hash2 = {}

        for i in nums1:
            if i not in hash1:
                hash1[i] = 1
            else:
                hash1[i] += 1
        
        for i in nums2:
            if i not in hash2:
                hash2[i] = 1
            else:
                hash2[i] += 1
            
        ans = []
        for i in hash1:
            if i in hash2:
                ans += [i]*(min(hash1[i],hash2[i]))
        
        return ans