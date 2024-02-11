# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def level(self,count,root,result):
        if root is None:
            return
        if len(result)<=count:
            result.append([])
        result[count].append(root.val)
        count+=1
        self.level(count,root.left,result)
        self.level(count,root.right,result)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        count = 0
        self.level(count,root,result)
        return result