class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1=sorted(nums1)
        n=len(nums1)
        
        if n%2!=0:
            mid=int((n+1)/2)
            return nums1[mid-1]
        else:
            mid=int(n/2)
            mid=(nums1[mid-1]+nums1[mid])/2
            return mid