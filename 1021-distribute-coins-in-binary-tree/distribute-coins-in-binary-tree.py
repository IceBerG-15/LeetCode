# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        self.moves = 0

        def postorder(node):
            if node is None:
                return 0

            left = postorder(node.left)
            right = postorder(node.right)
            balance = node.val + left + right -1
            self.moves += abs(balance)
            return balance

        postorder(root)
        return self.moves
        