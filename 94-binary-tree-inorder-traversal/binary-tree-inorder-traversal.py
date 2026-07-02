# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def inord(root):
            if root == None:
                return 
            inord(root.left)
            result.append(root.val)
            inord(root.right)

        inord(root)
        return result

            
        