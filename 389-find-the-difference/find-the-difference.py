class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dt = {}
        for i in t:
            if i not in dt:
                dt[i] = 1
            else:
                dt[i] +=1
        for i in s:
            if i not in dt:
                return i
            else:
                dt[i]-=1
        for i in dt:
            if dt[i]!=0:
                return i