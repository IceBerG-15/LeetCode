class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[0]<=target<=i[-1]:
                for j in i:
                    if j==target:
                        return True
        return False