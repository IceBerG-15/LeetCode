class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        total = 0
        n = 0
        while total<neededApples:
            n +=1
            total +=12*n*n
        return 8*n