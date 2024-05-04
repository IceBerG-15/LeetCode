class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        n = len(people)
        people.sort(reverse=True)
        left = 0
        right = n-1
        while left<=right:
            if people[left]+people[right]<=limit:
                boats +=1
                left +=1
                right -=1
            elif people[left]<=limit:
                boats +=1
                left +=1
            else:
                right -=1
        return boats