class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i,ch in enumerate(s):
            if ch=='(':
                stack.append(i)
            elif ch==')':
                if stack and s[stack[-1]]=='(':
                    stack.pop()
                else:
                    stack.append(i)
        ans = ''
        for i, ch in enumerate(s):
            if stack and i==stack[0]:
                stack.pop(0)
            else:
                ans+=ch
        return ans

        