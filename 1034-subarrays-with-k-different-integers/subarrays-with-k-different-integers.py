class Solution:
    def sliding(self,nums,k):
        n = len(nums)
        left = 0
        right = 0
        ans = 0
        mp = {}
        while right<n:
            if nums[right] not in mp:
                mp[nums[right]] = 1
            else:
                mp[nums[right]] +=1
            
            while len(mp)>k:
                mp[nums[left]] -=1
                if mp[nums[left]]==0:
                    del mp[nums[left]]
                left +=1
            ans +=right-left+1
            right +=1
        return ans

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.sliding(nums,k)-self.sliding(nums,k-1)