# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        parent = dict()
        queue = collections.deque([root])
        while queue:
            nodes = queue.copy()
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in [node.left, node.right]:
                    if not child: continue
                    parent[child] = node
                    queue.append(child)
        
        while len(nodes) > 1:
            nodes = set(parent[node] for node in nodes)
        return nodes.pop()
        
            