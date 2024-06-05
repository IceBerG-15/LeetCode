class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        initial = Counter(words[0])
        for word in words:
            initial &= Counter(word)

        return list(initial.elements())
        