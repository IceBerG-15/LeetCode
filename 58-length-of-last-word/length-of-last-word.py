class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.lstrip(' ')
        s = s.rstrip(' ')
        words = s.split(' ')
        return len(words[-1])