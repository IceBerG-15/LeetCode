class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        ans = n
        for i in citations:
            if i<ans:
                ans -=1
        return ans