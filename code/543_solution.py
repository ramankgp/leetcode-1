# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_dim = 0
        depths = collections.defaultdict(int)
        stack = [root] if root else []
        while stack:
            node = stack[-1]
            if node.left and node.left not in depths: 
                stack.append(node.left)
            elif node.right and node.right not in depths: 
                stack.append(node.right)
            else:
                stack.pop()
                l, r = depths[node.left], depths[node.right]
                depths[node] = 1 + max(l, r)
                max_dim = max(max_dim, l + r)
        return max_dim
                
    