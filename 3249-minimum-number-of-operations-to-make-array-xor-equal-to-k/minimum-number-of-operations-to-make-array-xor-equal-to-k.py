class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for i in nums:
            xor ^= i
        xor,k = bin(xor)[2:],bin(k)[2:]
        if len(xor)>len(k):
            k = '0'*(len(xor)-len(k)) + k
        else:
            xor = '0'*(len(k)-len(xor)) + xor
        
        ans = 0
        for i in range(len(xor)):
            if xor[i]!=k[i]:
                ans += 1
        return ans