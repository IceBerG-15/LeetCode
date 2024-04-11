class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k:
            return '0'
        stack = []
        for i in num:
            while stack and k>0 and i<stack[-1]:
                k-=1
                stack.pop()
            stack.append(i)
        while k>0:
            stack.pop()
            k-=1
        ans = ''.join(stack).lstrip('0')
        return ans if ans else '0'
