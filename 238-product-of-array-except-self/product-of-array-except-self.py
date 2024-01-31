class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_counter = 0
        ans = [0]*len(nums)
        n = len(nums)
        idx = 0
        for i,val in enumerate(nums):
            if val ==0:
                zero_counter +=1
                idx = i      
        if zero_counter>1:
            return ans
        elif zero_counter==1:
            prod = 1
            for i in range(n):
                if i==idx:
                    continue
                else:
                    prod *=nums[i]
            ans[idx] = prod
            return ans
        else:
            pre_prod = 1
            post_prod = 1
            for i in range(n):
                ans[i] = pre_prod
                pre_prod *=nums[i]
            for i in range(n-1,-1,-1):
                ans[i] *=post_prod
                post_prod *=nums[i]
            return ans
