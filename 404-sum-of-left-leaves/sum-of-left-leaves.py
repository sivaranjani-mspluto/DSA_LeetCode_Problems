# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def llsum(node,flag):
            if not node:
                return 0
            if not node.right and not node.left and flag:
                return node.val
            return ( llsum(node.left,True) + llsum(node.right,False) )
        return llsum(root,False)
        