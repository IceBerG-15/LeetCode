class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        key = s[0]
        count = 0
        for i in s[1:]:
            if key!=i:
                count +=1
                key = i
        return count

        