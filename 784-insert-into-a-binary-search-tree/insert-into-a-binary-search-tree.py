# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            root = TreeNode(val)
            return root
        if not root.left and val<root.val:
            root.left = TreeNode(val)
        elif not root.right and val>root.val:
            root.right = TreeNode(val)
        
        elif val<root.val:
            self.insertIntoBST(root.left,val)
        else:
            self.insertIntoBST(root.right,val)
        return root