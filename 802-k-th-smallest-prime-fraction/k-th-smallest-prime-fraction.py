class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        res = []
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                heappush(res, (-(arr[i] / arr[j]), arr[i], arr[j]))
                
                if len(res) > k:
                    heappop(res)
        
        return [res[0][1], res[0][2]]