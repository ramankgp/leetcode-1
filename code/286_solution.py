class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]: return
        m, n = len(rooms), len(rooms[0])
        
        gates = []
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    gates.append((r, c))
        
        def neighbors(r, c):
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == 2147483647:
                    yield (nr, nc)
        
        queue = collections.deque(gates)
        while queue:
            r, c = queue.popleft()
            for nr, nc in neighbors(r, c):
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))