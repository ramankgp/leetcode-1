class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        nrows, ncols = len(grid), len(grid[0])
        
        num_islands = 0
        visited = set()
        
        def get_neighbor(r, c):
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    yield (nr, nc)
        
        def tour(r, c):
            deque = collections.deque([(r, c)])
            while deque:
                r, c = deque.popleft() # bfs
                # r, c = deque.pop() # dfs
                if (r, c) in visited: continue
                visited.add((r, c))
                if grid[r][c] == '1':
                    deque.extend(get_neighbor(r, c))
        
        for r in range(nrows):
            for c in range(ncols):
                if (r, c) in visited: continue
                if grid[r][c] == '1':
                    tour(r, c)
                    num_islands += 1
        
        return num_islands