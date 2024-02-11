# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self,left,right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val!=right.val:
            return False
        return self.isMirror(left.left,right.right) and self.isMirror(left.right,right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root,root)