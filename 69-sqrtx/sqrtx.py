class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1 or x==2 or x==3:
            return 1
        left = 1
        right = x
        while left<=right:
            mid = (left+right)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                left = mid+1
            else:
                right = mid-1
        return right