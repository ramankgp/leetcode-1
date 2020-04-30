class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = sorted(map(abs, (x, y)))
        memo = {(0,0):0}
        queue = collections.deque([(0,0)])
        
        def get_next(loc):
            xx, yy = loc
            for dx, dy in [(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]:
                nx, ny = xx + dx, yy + dy
                if (nx, ny) in memo: continue
                if nx < -2 or ny < -2 or nx > x + 2 or ny > y + 2: continue
                if nx - ny > 2: continue
                yield (nx, ny)
        
        step = 0
        while (x,y) not in memo:
            step += 1
            for _ in range(len(queue)):
                loc = queue.popleft()
                for next_loc in get_next(loc):
                    memo[next_loc] = step
                    queue.append(next_loc)
        return memo[(x,y)]
        
        
        