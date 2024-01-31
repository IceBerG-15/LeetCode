class Solution:
    def checkValidString(self, s: str) -> bool:

        openbrace = 0
        closebrace = 0
        slen = len(s)-1
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='*':
                openbrace +=1
            else:
                openbrace -=1
            if s[slen-i]==')' or s[slen-i]=='*':
                closebrace +=1
            else:
                closebrace -=1
            if openbrace<0 or closebrace<0:
                return False
        return True