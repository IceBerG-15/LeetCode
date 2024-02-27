class Solution:
    def check(self,word,temp):
        ptr = list(temp)
        for i in word:
            if i in ptr:
                ptr.remove(i)
                if len(ptr)==0:
                    return True
        return False
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        chars = []
        for i in licensePlate.lower():
            if i.isalpha():
                chars.append(i)
        minlen = inf
        ans = ''
        for word in words:
            if self.check(word,chars):
                if minlen>len(word):
                    minlen = len(word)
                    ans = word        
        return ans