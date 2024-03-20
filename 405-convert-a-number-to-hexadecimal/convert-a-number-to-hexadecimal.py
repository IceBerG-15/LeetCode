class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num<0:
            num = (1<<32)+num
        hex= ''
        while num>0:
            r = num%16
            num = num//16
            if 0<=r<=9:
                hex += str(r)
            elif r==10:
                hex += 'a'
            elif r==11:
                hex += 'b'
            elif r==12:
                hex += 'c'
            elif r==13:
                hex += 'd'
            elif r==14:
                hex +='e'
            else:
                hex+='f'
            
        return hex[::-1]
    