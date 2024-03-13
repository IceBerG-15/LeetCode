class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = [0]*26
        distinct = set(word)
        n = len(distinct)
        if n==1:
            return True
        for i in word:
            freq[ord(i)-ord('a')] +=1
        freq.sort()
        return (freq[25]==1 or
                (freq[25]-freq[24]==1 and freq[26-n]==freq[24]) or
                (freq[26-n]==1 and freq[25]==freq[27-n])
                )