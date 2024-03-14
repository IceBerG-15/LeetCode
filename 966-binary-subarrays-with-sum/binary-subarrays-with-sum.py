class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def helper(x):
            if x<0: return 0

            ans = 0
            l,curr_sum = 0,0
            for i in range(len(nums)):
                curr_sum +=nums[i]
                while curr_sum>x:
                    curr_sum -= nums[l]
                    l+=1
                ans += i-l+1
            return ans
        
        return helper(goal)-helper(goal-1)