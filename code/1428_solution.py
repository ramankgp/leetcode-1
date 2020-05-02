# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n, m = binaryMatrix.dimensions()
        r = 0
        c = m-1
        last_c = -1
        while r < n and c >= 0:
            if binaryMatrix.get(r,c):
                last_c = c
                c -= 1
            else:
                r += 1
        return last_c
