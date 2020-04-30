class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k: return 0
        # window = dict()
        max_len = 0
        # l = 0
        # for r, char in enumerate(s): # O(N)
            # window[char] = window.get(char, 0) + 1
            # while len(window) > k: # O(N)
            #     window[s[l]] -= 1
            #     if window[s[l]] == 0: window.pop(s[l])
            #     l += 1
            # max_len = max(max_len, r-l+1)
        l = -1            
        # for r, char in enumerate(s): # O(N)
        #     window[char] = r
        #     if len(window) > k: 
        #         l = min(window.values()) # O(k)
        #         window.pop(s[l])
        #     max_len = max(max_len, r-l)
        
        window = collections.OrderedDict()
        for r, char in enumerate(s): # O(N)
            window[char] = r
            window.move_to_end(char)
            if len(window) > k: _, l = window.popitem(last=False) # O(1)
            max_len = max(max_len, r-l)
        return max_len
            