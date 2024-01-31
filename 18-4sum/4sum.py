class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        if len(nums)<4:
            return []
        elif len(nums)==4:
            if sum(nums)==target:
                ans.append(nums)
            else:
                return []
        else:
            nums.sort()
            n = len(nums)-1
            for i in range(n):
                for j in range(i+1,n):
                    left = j+1
                    right = n
                    while left<right:
                        s = nums[i]+nums[j]+nums[left]+nums[right]
                        if s==target:
                            l=[nums[i],nums[j],nums[left],nums[right]]
                            if l not in ans:
                                ans.append(l)
                            left +=1
                        elif s>target:
                            right -=1
                        else:
                            left+=1
        return ans