class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        def check(n):
            l = list(map(int,list(str(n))))
            if 0 in l:
                return False
            for i in l:
                if n%i!=0:
                    return False
            return True
        
        ans = []
        for i in range(left,right+1):
            if check(i):
                ans.append(i)
            
        return ans
        