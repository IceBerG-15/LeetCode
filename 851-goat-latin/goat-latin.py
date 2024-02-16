class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a','e','i','o','u']
        words = sentence.split(' ')
        ans = ['']*len(words)
        for i in range(len(words)):
            if words[i][0].lower() in vowels:
                ans[i] = words[i]+'ma'
            else:
                ans[i] = words[i][1:]+words[i][0]+'ma'
            ans[i] = ans[i]+('a'*(i+1))
        ans = ' '.join(ans)
        return ans