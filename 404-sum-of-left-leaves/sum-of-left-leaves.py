# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def pre(root,isLeft):
            if not root:
                return 0
            if not root.left and not root.right and isLeft:
                return root.val
            return pre(root.left,True)+pre(root.right,False)
        return pre(root,False)
        