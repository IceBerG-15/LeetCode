# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        nums = []

        def dfs(node,curr_str):
            if not node:
                return 
            if not node.left and not node.right:
                nums.append(int(curr_str + str(node.val)))
                return
            curr_str += str(node.val)
            dfs(node.left,curr_str)
            dfs(node.right,curr_str)
        
        dfs(root,'')
        return sum(nums)
        
        return dfs(root,0)
        