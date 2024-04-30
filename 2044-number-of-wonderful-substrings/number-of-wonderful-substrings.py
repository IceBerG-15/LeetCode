class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0]*1024
        ans = 0
        prefix_xor = 0
        count[prefix_xor] = 1

        for i in word:
            char_idx = ord(i)-ord('a')
            prefix_xor ^= 1<<char_idx
            ans += count[prefix_xor]
            for j in range(10):
                ans += count[prefix_xor ^ (1<<j) ]
            count[prefix_xor] +=1
        
        return ans