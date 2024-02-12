class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1 or n==2:
            return 0
        primes = [True]*n
        primes[0]=primes[1]=False
        count = 1
        for i in range(2,int(n**0.5)+1):
            if primes[i] is True:
                for j in range(i*i,n,i):
                    if primes[j] is True:
                        count +=1
                    primes[j] = False
        return n-count-1