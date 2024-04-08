class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        hashm = {1:0,0:0}
        for i in students:
            hashm[i]+=1
        for i in sandwiches:
            if hashm[i]==0:
                return n
            hashm[i]-=1
            n-=1
        return n