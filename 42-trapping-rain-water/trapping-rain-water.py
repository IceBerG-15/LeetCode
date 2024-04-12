class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left = 0
        right = n-1
        lmax = height[left]
        rmax = height[right]
        ans = 0
        while left<right:
            if lmax<=rmax:
                ans += lmax-height[left]
                left+=1
                lmax = max(lmax,height[left])
            else:
                ans += rmax-height[right]
                right-=1
                rmax = max(rmax,height[right])
        return ans