"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew={}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            #create a new copy node
            copyNode = Node(node.val)
            oldToNew[node]=copyNode
            for n in node.neighbors:
                copyNode.neighbors.append(dfs(n))
            return copyNode
        if node!=None:
            return dfs(node)
        else:
            return None
    

    