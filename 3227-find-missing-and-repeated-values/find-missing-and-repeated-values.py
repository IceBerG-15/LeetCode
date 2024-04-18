class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        n = len(grid)
        l = [False]*((n**2)+1)
        for i in range(n):
            for j in range(n):
                m = grid[i][j]
                if l[m]!=False:
                    ans.append(m)
                l[m]=True
        for i in range(1,len(l)):
            if l[i]==False:
                ans.append(i)
        return ans
        