class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=='':
            return []
        keyboard = {"2": "abc","3": "def","4": "ghi","5": "jkl","6": "mno","7": "pqrs","8": "tuv","9": "wxyz"}

        ans = []
        def backtrack(com,next_digit):
            if not next_digit:
                ans.append(com)
                return
            for letter in keyboard[next_digit[0]]:
                backtrack(com+letter,next_digit[1:])
        backtrack('',digits)
        return ans
            
