class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        curr_max = -1
        for i in arr[::-1]:
            ans.append(curr_max)
            if i>curr_max:
                curr_max = i
        return ans[::-1]