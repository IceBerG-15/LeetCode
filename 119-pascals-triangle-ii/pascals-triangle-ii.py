class Solution:
    def getRow(self, numRows: int) -> List[int]:
        if numRows==0:
            return [1]
        elif numRows==1:
            return [1,1]
        ans = [[1],[1,1]]

        def func(a):
            l = []
            for i in range(len(a)-1):
                l.append(a[i]+a[i+1])
            l = [1]+l+[1]
            ans.append(l)

        for _ in range(numRows-1):
            func(ans[-1])
        return ans[-1]