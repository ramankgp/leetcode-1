# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = collections.deque([root])
        while queue:
            parent = dict()
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in [node.left, node.right]:
                    if not child: continue
                    queue.append(child)
                    parent[child.val] = node
            if (x in parent) ^ (y in parent): return False
            if x in parent and y in parent:
                if parent[x] == parent[y]: return False
                else: return True
        return False