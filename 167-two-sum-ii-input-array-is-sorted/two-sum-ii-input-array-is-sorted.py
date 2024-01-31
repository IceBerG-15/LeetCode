class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        left = 0
        right = len(numbers)-1
        while left<right:
            s = numbers[left]+numbers[right]
            if s==target:
                ans.append(left+1)
                ans.append(right+1)
                return ans
            elif s>target:
                right -=1
            else:
                left +=1
        return []