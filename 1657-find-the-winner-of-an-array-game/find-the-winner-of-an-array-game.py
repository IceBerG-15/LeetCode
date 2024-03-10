class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        count = 0
        winner = arr[0]
        for i in arr[1:]:
            if i>winner:
                winner = i
                count =1
            else:
                count +=1
            if count==k:
                break
        return winner

