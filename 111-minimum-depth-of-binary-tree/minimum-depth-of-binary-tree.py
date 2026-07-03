# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # def dfs_minpath(node):
        #     if not node:
        #         return 0
        #     if not node.left:
        #         return 1 + dfs_minpath(node.right)
        #     if not node.right:
        #         return 1 + + dfs_minpath(node.left)
        #     return 1 + min(dfs_minpath(node.left),dfs_minpath(node.right))
        # return dfs_minpath(root)

        def bfs_minpath(root):
            if not root:
                return 0
            queue = deque([(root,1)])
            level =1
            while queue:
                node,level = queue.popleft()
                #if its a left node
                if not node.left and not node.right:
                    return level
                if node.left:
                    queue.append((node.left,level+1))
                if node.right:
                    queue.append((node.right,level+1))
            return 0
        return bfs_minpath(root)