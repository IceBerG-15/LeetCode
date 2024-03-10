class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = sorted([d/s for d,s in zip(dist,speed)])
        ans = 0
        for i in range(len(time)):
            if time[i]<=i:
                break
            ans +=1
        return ans