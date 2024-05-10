class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = {}
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                fractions[arr[i]/arr[j]] = [arr[i],arr[j]]  
        frac = sorted(fractions)
        return fractions[frac[k-1]]