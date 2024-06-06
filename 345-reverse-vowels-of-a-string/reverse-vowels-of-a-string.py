class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ''
        for i,val in enumerate(s):
            if val in 'aeiouAEIOU':
                s[i] = '_'
                vowels += val
        
        n = len(vowels)-1
        for i,val in enumerate(s):
            if val=='_':
                s[i] = vowels[n]
                n -= 1
        
        return ''.join(s)
        