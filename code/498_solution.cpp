class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        indices = [(i,j) for i in range(m) for j in range(n)]
        indices.sort(key=lambda x: (sum(x), (x[1], x[0])[sum(x) & 1], (x[1], x[0])[sum(x) & 0]))
        return [matrix[i][j] for [i, j] in indices]
