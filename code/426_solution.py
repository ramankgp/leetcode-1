"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root
        stack = []
        trav = root
        head = Node(None)
        prev = None
        # iterative in order traversal
        while trav or stack:
            while trav:
                stack.append(trav)
                trav = trav.left            
            trav = stack.pop()
            # grab a reference to the first node
            if not head.right: head.right = trav
            # pred, succ links
            if prev: prev.right, trav.left = trav, prev
            prev = trav
            trav = trav.right
        
        # make circular
        prev.right = head.right
        head.right.left = prev
    
        return head.right
