class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return n
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        for i in range(n//2,n+1):
            if sum(arr[:i])==sum(arr[i-1:]):
                return i
        return -1