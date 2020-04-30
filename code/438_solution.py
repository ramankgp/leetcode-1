class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        solution = []
        if len(s) < len(p): return solution
        n = len(p)
        req_freq = collections.Counter(p)
        window = collections.Counter([c for c in s[:n] if c in req_freq])
        if window == req_freq: solution.append(0)
        for i, char in enumerate(s[n:], n):
            if char in req_freq:
                window.update(char)
            if s[i - n] in req_freq:
                window.subtract(s[i - n])
            if window == req_freq: solution.append(i - n + 1)
        return solution