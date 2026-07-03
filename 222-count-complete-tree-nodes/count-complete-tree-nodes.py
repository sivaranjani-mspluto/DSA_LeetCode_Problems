# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            c=0
            if not root:
                return c
            queue = deque([root])
            while queue:
                node = queue.popleft()
                c+=1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return c
        return bfs(root)
            
        