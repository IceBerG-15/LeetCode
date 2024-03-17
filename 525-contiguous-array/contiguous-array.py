class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = []
        s = 0
        hash_map = {0:-1}
        for i in nums:
            if i==1:
                s +=1
            else:
                s-=1
            prefix_sum.append(s)

        ans = 0
        for i in range(len(prefix_sum)):
            if prefix_sum[i] not in hash_map:
                hash_map[prefix_sum[i]] = i
            else:
                ans = max(ans,i-hash_map[prefix_sum[i]])
        
        
        return ans
        