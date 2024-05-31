class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        char_map = Counter(chars)
        
        for word in words:
            word_map = Counter(word)
            c = True
            for ch in word_map:
                if ch not in char_map:
                    c = False
                    break
                elif word_map[ch] >char_map[ch]:
                    c = False
                    break

            if c:
                ans += len(word)
            
        
        return ans