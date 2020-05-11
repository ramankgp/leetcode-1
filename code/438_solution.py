class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        solution = []
        if len(s) < len(p): return solution
        n = len(p)
        req_freq = collections.Counter(p)
        window = collections.Counter(filter(lambda x: x in req_freq, s[:n]))
        # if window == req_freq: solution.append(0)
        # for i, char in enumerate(s[n:], n):
        #     if char in req_freq:
        #         window.update(char)
        #     if s[i - n] in req_freq:
        #         window.subtract(s[i - n])
        #     if window == req_freq: solution.append(i - n + 1)

        # update 2020-05-10 use a counter to avoid a collection equality check. 
        to_match = len(req_freq)
        for char in req_freq: to_match -= window[char] == req_freq[char]
        if not to_match: solution.append(0)
        for i, (in_char, out_char) in enumerate(zip(s[n:], s), n):
            if in_char in req_freq: 
                if window[in_char] == req_freq[in_char]: to_match += 1
                if window[in_char] + 1 == req_freq[in_char]: to_match -= 1
                window.update(in_char)
            if out_char in req_freq: 
                if window[out_char] == req_freq[out_char]: to_match += 1
                if window[out_char] - 1 == req_freq[out_char]: to_match -= 1
                window.subtract(out_char)
            if not to_match: solution.append(i - n + 1)
        return solution