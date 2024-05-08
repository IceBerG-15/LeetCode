class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranking = sorted(score,reverse = True)
        ranks = {}
        for i,val in enumerate(ranking):
            if i<3:
                if i==0:
                    ranks[val] = 'Gold Medal'
                elif i==1:
                    ranks[val] = 'Silver Medal'
                else:
                    ranks[val] = 'Bronze Medal'
            else:
                ranks[val] = str(i+1)
        
        ans = []
        for i in score:
            ans.append(ranks[i])
        return ans
