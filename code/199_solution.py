# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return 
        
        current_level = 0
        queue = collections.deque([(root, 1)])
        result = []
        while queue:
            node, node_level = queue.popleft()
            if node_level > current_level:
                result.append(node.val)
                current_level += 1
            
            if node.right: 
                queue.append((node.right, node_level + 1))
            if node.left:
                queue.append((node.left, node_level + 1))
        return result