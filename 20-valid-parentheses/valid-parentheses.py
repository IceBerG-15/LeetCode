class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            elif stack:
                if i==')' and stack[-1]=='(':
                    stack.pop()
                elif i==']' and stack[-1]=='[':
                    stack.pop()
                elif i=='}' and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            else:
                return False
        if stack:
            return False
        return True