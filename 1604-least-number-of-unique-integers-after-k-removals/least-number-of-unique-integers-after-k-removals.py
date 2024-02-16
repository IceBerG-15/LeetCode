class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if k==0:
            return len(set(arr))
        elif k==len(arr):
            return 0
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] +=1
        elements = sorted(freq.items(),key=lambda x:x[1])
        for key,value in elements:
            if value<=k:
                k -= value
                del freq[key]
            else:
                break
        return len(freq)