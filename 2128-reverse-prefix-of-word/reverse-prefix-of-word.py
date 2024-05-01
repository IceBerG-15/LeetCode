class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        idx = word.index(ch)
        ch = word[:idx+1]
        word = ch[::-1]+word[idx+1:]
        return word