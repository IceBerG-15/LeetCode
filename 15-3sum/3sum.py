class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums)==3:
            if sum(nums)==0:
                ans.append(nums) 
        else:
            nums.sort()
            n = len(nums)
            for idx,val in enumerate(nums):
                if idx>0 and val==nums[idx-1]:
                    continue
                left = idx+1
                right = n-1
                while left<right:
                    s = val+nums[left]+nums[right]
                    if s==0:
                        ans.append([val,nums[left],nums[right]])
                        left+=1
                        while nums[left]==nums[left-1] and left<right:
                            left+=1
                    elif s>0:
                        right-=1
                    else:
                        left+=1
        return ans