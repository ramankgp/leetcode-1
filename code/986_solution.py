class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        def intersect(i1, i2):
            l = max(i1[0], i2[0])
            r = min(i1[1], i2[1])
            return [l, r] if l <= r else None
        
        output = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            intersection = intersect(A[i], B[j])
            if intersection: output.append(intersection)
            if A[i][1] < B[j][1]: i += 1
            else: j += 1
        return output
                