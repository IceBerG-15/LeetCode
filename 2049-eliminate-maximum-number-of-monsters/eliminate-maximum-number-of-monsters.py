class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(dist)):
            time.append(dist[i]/speed[i])
        time.sort()
        ans = 0
        for i in range(len(time)):
            if time[i]<=i:
                break
            ans +=1
        return ans