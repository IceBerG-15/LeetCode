class Solution:
    def count(self,n,word):
        if n==0:
            return word
        d = []
        i = 0
        while i<len(word):
            j = i
            count = 0
            while j<len(word) and word[i]==word[j]:
                count +=1
                j +=1
            d.append((word[i],count))
            i = j 
        ans = ''
        for key,val in d:
            ans +=(str(val)+key)
        print(ans)
        return self.count(n-1,ans)

    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        return self.count(n-1,'1')