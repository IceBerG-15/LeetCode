class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1!='' and num2!='':
            s = int(num1)*int(num2)
        else:
            s = 0
        return str(s)