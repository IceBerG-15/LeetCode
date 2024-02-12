class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1 or n==2:
            return 0
        l = [True]*n
        l[0]=l[1]=False
        p = 2
        while p**2<=n:
            if l[p] is True:
                for i in range(p*p,n,p):
                    l[i] = False
            p+=1
        count = 0
        for i in l:
            if i is True:
                count +=1
        return count