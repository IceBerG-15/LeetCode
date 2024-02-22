class Solution:
    def divide(self, nums:dict, div:dict, count:int)->int:
        #base case
        if len(nums)==0:
            return -1
        smallest = min(nums)
        c = 0
        for i in div:
            if i%smallest!=0:
                break
            c +=1
        if c==len(div):
            return count
        else:
            count +=nums[smallest]
            nums.pop(smallest)
            return self.divide(nums,div,count)

    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] =1
            else:
                d[i] +=1

        div = {}
        for i in numsDivide:
            if i not in div:
                div[i] =1
            else:
                div[i] +=1
        ans = self.divide(d,div,0)
        return ans