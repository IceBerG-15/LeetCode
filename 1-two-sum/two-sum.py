class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out=[]
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if i==j:
                    continue
                else:
                    if nums[i]+nums[j]==target:
                        out.append(i)
                        out.append(j)  
                        break
            if len(out)!=0:
                break
        return(out)