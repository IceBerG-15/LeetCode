class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        return (sum(salary)-min(salary)-max(salary))/(n-2)