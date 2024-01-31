class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(n+1):
            if i==0:
                continue
            else:
                ans[i] = self.hammingWeight(i)
        return ans

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n>0:
            if n%2==1:
                count = count+1
            n = n//2
        return count