class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq = '123456789'
        ans = []
        n = len(seq)
        for i in range(n):
            for j in range(i+1,n+1):
                num = int(seq[i:j])
                if low<=num<=high:
                    ans.append(num)
        ans.sort()
        return ans