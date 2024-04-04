class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        ans = [[1],[1,1]]

        def func(a):
            l = []
            for i in range(len(a)-1):
                l.append(a[i]+a[i+1])
            l = [1]+l+[1]
            ans.append(l)

        for _ in range(numRows-2):
            func(ans[-1])
        return ans