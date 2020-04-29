# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path_sum = float('-inf')
        
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.max_path_sum = max(self.max_path_sum, l+r+node.val)
            return max(0, node.val + max(l,r))
        
        dfs(root)
        return self.max_path_sum