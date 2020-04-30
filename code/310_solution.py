class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(candidate):
            count = 0
            for ch in candidate:
                if ch == '(': count += 1
                if ch == ')': count -= 1
                if count < 0: return False
            return count == 0
        
        def get_min_removals():
            l = r = 0
            for ch in s:
                if ch == '(': l += 1
                if ch == ')':
                    if l: l -= 1
                    else: r += 1
            return l, r
        
        def get_next(candidate, loc, last_rm, l, r):
            for i, ch in enumerate(candidate[loc:], loc):
                if ch not in '()': continue
                if i and candidate[i-1] == ch: continue
                if last_rm == '(' and ch == ')': continue
                if not l and ch == '(': continue
                if not r and ch == ')': continue
                yield candidate[:i] + candidate[i+1:], i, ch, l-int(ch=='('), r-int(ch==')')

        l, r = get_min_removals()
        results = []
        candidates = collections.deque([(s, 0, '', l, r)])
        while candidates: 
            # candidate = candidates.popleft() # BFS
            candidate = candidates.pop() # DFS
            if sum(candidate[-2:]) == 0 and valid(candidate[0]):
                results.append(candidate[0])
            else:
                candidates.extend(get_next(*candidate))
        return results