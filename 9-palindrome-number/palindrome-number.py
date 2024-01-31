class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        i=x
        while i!=0:
            p=int(i%10)
            rev=int(rev*10+p)
            i=int(i/10)
        if rev==x:
            return True
        else:
            return False