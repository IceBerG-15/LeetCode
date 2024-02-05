class MagicDictionary:

    def __init__(self):
        self.dictionary = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.dictionary = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.dictionary:
            if len(word)!=len(searchWord):
                continue
            c = 0
            for j in range(len(word)):
                if word[j]!=searchWord[j]:
                    c +=1
            if c==1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)