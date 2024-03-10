class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        curr = 1
        ans = []
        for num in target:
            while curr<num:
                ans.append('Push')
                ans.append('Pop')
                curr +=1
            ans.append('Push')
            curr +=1
        return ans