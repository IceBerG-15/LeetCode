class Solution:
    def count(self,n,word):
        if n==0:    #base condition
            return word
        d = []
        i = 0
        while i<len(word):
            j = i
            count = 0
            while j<len(word) and word[i]==word[j]:  #checking for more consecutive cases
                count +=1
                j +=1
            d.append((word[i],count))  #appending the tuple which has a value like (character,count) into the list.
            i = j 
        word = ''
        for key,val in d:
            word +=(str(val)+key)   #creating string from the list
        return self.count(n-1,word)  #recursive call to the count function for next iteration

    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        return self.count(n-1,'1')