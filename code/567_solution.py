class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        if len(s) < len(p):  return False
        n = len(p)
        req_freq = collections.Counter(p)
        window = collections.Counter([c for c in s[:n] if c in req_freq])
        to_match = len(req_freq)
        for char in req_freq: to_match -= window[char] == req_freq[char]
        if not to_match: return True
        for in_char, out_char in zip(s[n:], s[:]):
            if in_char in req_freq: 
                if window[in_char] == req_freq[in_char]: to_match += 1
                if window[in_char] == req_freq[in_char] - 1: to_match -= 1
                window[in_char] += 1
            if out_char in req_freq: 
                if window[out_char] == req_freq[out_char]: to_match += 1
                if window[out_char] == req_freq[out_char]+1: to_match -= 1
                window[out_char] -= 1
            if not to_match: return True
        return False