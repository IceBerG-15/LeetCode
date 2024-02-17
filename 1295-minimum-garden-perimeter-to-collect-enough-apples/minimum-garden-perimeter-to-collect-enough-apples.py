class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        n = 0
        while neededApples>0:
            n +=1
            neededApples-=12*n*n
        return 8*n