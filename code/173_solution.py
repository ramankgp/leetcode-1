# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root = root
        self._reset()

    def _reset(self):
        self.node = self.root
        self.stack = []
        
    def __iter__(self):
        self._reset()
        return self
    
    def __next__(self) -> int:
        """ Return the next smallest number """
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left
        self.node = self.stack.pop()
        ret_val = self.node.val
        self.node = self.node.right
        return ret_val
    
    def next(self):
        return self.__next__()        

    def hasNext(self) -> bool:
        """ Return whether we have a next smallest number """
        return self.stack or self.node
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()