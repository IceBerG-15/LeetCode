class Solution:
    def reverseVowels(self, s: str) -> str:
        # Convert the string to a list to allow modification of individual characters
        s = list(s)
        
        # Initialize an empty string to store the vowels
        vowels = ''
        
        # Iterate over the string to identify vowels and replace them with underscores
        for i, val in enumerate(s):
            if val in 'aeiouAEIOU':  # Check if the character is a vowel (case-insensitive)
                s[i] = '_'          # Replace vowel with an underscore in the list
                vowels += val        # Append the vowel to the vowels string
        
        # Set the index to the last character of the vowels string
        n = len(vowels) - 1
        
        # Iterate over the string again to replace underscores with reversed vowels
        for i, val in enumerate(s):
            if val == '_':           # Check if the character is an underscore
                s[i] = vowels[n]     # Replace underscore with the corresponding vowel from the end
                n -= 1               # Move to the previous vowel in the vowels string
        
        # Convert the list back to a string and return it
        return ''.join(s)
