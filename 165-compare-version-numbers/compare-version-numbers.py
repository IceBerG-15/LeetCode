class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        rev1 = version1.split('.')
        rev2 = version2.split('.')

        n = len(rev1)
        m = len(rev2)
        if n>m:
            for _ in range(n-m):
                rev2.append('0')
        else:
            for _ in range(m-n):
                rev1.append('0')
        
        for i in range(len(rev1)):
            if int(rev1[i])==int(rev2[i]):
                continue
            elif int(rev1[i])>int(rev2[i]):
                return 1
            else:
                return -1

        return 0