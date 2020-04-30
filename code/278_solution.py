# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n 
        while l < h:
            m = (l + h) // 2
            if isBadVersion(m):
                h = m
            else:
                l = m + 1
        return l 