# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = None
        stack = []
        for val in preorder:
            node = TreeNode(val)
            if not root:
                root = node
            elif val < stack[-1].val:
                stack[-1].left = node
            else:
                while stack and stack[-1].val < val:
                    pnode = stack.pop()
                pnode.right = node
            stack.append(node)
        return root