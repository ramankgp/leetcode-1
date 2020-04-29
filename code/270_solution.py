# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        node = root
        candidate = node.val 
        while node:
            candidate = min((candidate, node.val), key=lambda x: abs(x - target))
            if node.val < target:
                node = node.right
            elif node.val > target:
                node = node.left
            else:
                return node.val
        return candidate
    