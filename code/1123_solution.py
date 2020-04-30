# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        parent = dict()
        queue = [root]
        
        while queue:
            next_level = []
            for node in queue:
                if node.left: 
                    next_level.append(node.left)
                    parent[node.left] = node
                if node.right: 
                    next_level.append(node.right)
                    parent[node.right] = node
            if not next_level: break
            queue = next_level
        
        while len(queue) > 1:
            queue = set(parent[node] for node in queue)
        
        return queue.pop()
                        
                