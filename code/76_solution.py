class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        target = collections.Counter(t)
        window = collections.defaultdict(int)
        min_len, min_l, min_r = n, 0, n
        to_match = len(target)
        
        filtered_s = [(i, c) for i, c in enumerate(s) if c in target]
        if not filtered_s: return ""
        # l = 0
        # for r, c in enumerate(s):
        l_idx = 0
        l = filtered_s[l_idx][0]
        for r, c in filtered_s:
            # if c not in target: continue
            window[c] += 1
            if window[c] == target[c]: to_match -= 1
            
            if not to_match:
                # while s[l] not in target or window[s[l]] > target[s[l]]:
                #     if s[l] in window:
                #         window[s[l]] -= 1
                #     l += 1
                while window[s[l]] > target[s[l]]:
                    window[s[l]] -= 1
                    l_idx += 1
                    l = filtered_s[l_idx][0]
                window_len = r - l + 1
                if min_len > window_len:
                    min_len = window_len
                    min_l, min_r = l, r
        return "" if to_match else s[min_l:min_r+1]
                
                    