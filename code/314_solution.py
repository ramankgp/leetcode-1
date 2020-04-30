# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return 
        gpby = collections.defaultdict(list)
        def dfs(node, x, y):
            gpby[x].append((y, node.val))
            if node.left: dfs(node.left, x-1, y+1)
            if node.right: dfs(node.right, x+1, y+1)
            
        dfs(root,0,0)
        return [[t[1] for t in sorted(gpby[x], key=lambda t:t[0])] for x in sorted(gpby)]