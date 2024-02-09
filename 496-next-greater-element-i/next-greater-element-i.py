class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            j = nums2.index(i)+1
            while j<len(nums2) and nums2[j]<i:
                j+=1
            if j<len(nums2) and nums2[j]>i:
                ans.append(nums2[j])
            else:
                ans.append(-1)
        return ans