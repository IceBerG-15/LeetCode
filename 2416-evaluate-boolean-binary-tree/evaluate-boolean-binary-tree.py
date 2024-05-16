# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        preord = []
        
        def preorder(node):
            if node:
                preord.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        stack = []
        for i in preord[::-1]:
            if i==0 or i==1:
                stack.append(i)
            elif i==2 or i==3:
                a = stack.pop()
                b = stack.pop()
                if i==2:
                    stack.append(a or b)
                else:
                    stack.append(a and b)
            
            
        return True if stack[0]==1 else False