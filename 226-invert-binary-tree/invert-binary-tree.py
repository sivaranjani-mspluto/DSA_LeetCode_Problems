# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # def invert(node):
        #     if not node:
        #         return
        #     if node.left:
        #         node.left = invert(node.right)
        #     if node.right:
        #         node.right = invert(node.left)
        #     return node
        # return invert(root)

        #FIRST SWAP AND THEN INVERT THEM INDIVIDUALLY
        if not root:
            return 
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



        