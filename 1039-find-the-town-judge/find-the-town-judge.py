class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        possible = [0]*(n+1)
        possible[0] = 0
        for i in trust:
            possible[i[0]] -=1
            possible[i[1]] +=1
        for i in range(1,n+1):
            if possible[i]==n-1:
                return i
        return -1
        