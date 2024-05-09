class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness,reverse = True)
        ans = 0
        c = 0
        for i in happiness[:k]:
            if i-c<0:
                continue
            else:
                ans += i-c
                c +=1
        return ans