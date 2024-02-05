class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i.isnumeric():
                stack.append(int(i))
            elif i[1:].isnumeric():
                stack.append(int(i))
            elif i=='C':
                stack.pop()
            elif i=='D':
                a = stack[-1]
                stack.append(2*a)
            elif i=='+':
                a = stack[-1]
                b = stack[-2]
                stack.append(a+b)
        return sum(stack)