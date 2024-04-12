class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        n = num/2
        left = 0
        right = n
        while left<=right:
            mid = (left+right)//2
            if mid*mid==num:
                return True
            elif mid*mid<num:
                left = mid+1
            else:
                right = mid-1
        return False