# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result=[]
        def dfs_path(node,curr_path):
            if not node:
                return 
            if curr_path:
                curr_path += "->"+ str(node.val)
            else:
                curr_path = str(node.val)
            #if it is a leaf node -- save the curr_path
            if not node.left and not node.right:
                result.append(curr_path)
            else:
                if node.left:
                    dfs_path(node.left,curr_path)
                if node.right:
                    dfs_path(node.right,curr_path)

        dfs_path(root,[])
        return result

        