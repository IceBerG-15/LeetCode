# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def level(self,root,count,result):
        if root is None:
            return
        if len(result)<=count:
            result.append([])
        result[count].append(root.val)
        count+=1
        self.level(root.left,count,result)
        self.level(root.right,count,result)

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        count = 0
        self.level(root,count,result)
        for i in range(len(result)):
            if i%2!=0:
                result[i]=result[i][::-1]
        return result