class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = sorted(map(abs, (x, y)))
        memo_s = {(0,0):0}
        memo_t = {(x,y):0}
        queue_s = collections.deque([(0,0)])
        queue_t = collections.deque([(x,y)])
        
        def get_next(loc, memo):
            xx, yy = loc
            for dx, dy in [(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]:
                nx, ny = xx + dx, yy + dy
                if (nx, ny) in memo: continue
                if nx < -2 or ny < -2 or nx > x + 2 or ny > y + 2: continue
                if nx - ny > 2: continue
                yield (nx, ny)
        
        step = 0
        while True:
            step += 1
            # bfs from source
            for _ in range(len(queue_s)):
                loc = queue_s.popleft()
                if loc in memo_t: return memo_s[loc] + memo_t[loc]
                for next_loc in get_next(loc, memo_s):
                    memo_s[next_loc] = step
                    queue_s.append(next_loc)
            # bfs from target
            for _ in range(len(queue_t)):
                loc = queue_t.popleft()
                if loc in memo_s: return memo_s[loc] + memo_t[loc]
                for next_loc in get_next(loc, memo_t):
                    memo_t[next_loc] = step
                    queue_t.append(next_loc)
