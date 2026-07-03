# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs_minpath(node):
            if not node:
                return 0
            if not node.left:
                return 1 + dfs_minpath(node.right)
            if not node.right:
                return 1 + + dfs_minpath(node.left)
            return 1 + min(dfs_minpath(node.left),dfs_minpath(node.right))
        return dfs_minpath(root)