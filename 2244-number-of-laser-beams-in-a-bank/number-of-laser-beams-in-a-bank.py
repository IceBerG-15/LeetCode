class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers = []
        for i in bank:
            count = i.count('1')
            if count!=0:
                lasers.append(count)
        ans = 0
        for i in range(len(lasers)-1):
            ans += lasers[i]*lasers[i+1]
        return ans