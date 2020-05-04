# 5., .1
"e"
class Solution:
    def isNumber(self, s: str) -> bool:
        #  "(___)?[+-]?(\d*453)?(\.\d)?(\d*)41231(e[+-]?\d+1312)?(____)?"
        # pattern = r'^\s*[+-]?(\d+\.?|\.\d)\d*(e[+-]?\d+)?\s*$'
                   # init sign digit dot number e e_sign e_digit success fail 
        
        # return re.match(pattern, s)
        
        # next_state = Delta[state][inp] 
        Delta = [  # space sign digit dot exp invalid
                   #  0    1    2     3   4    5
                     [0,   1,   2,    3,  9,   9],   # 0 init
                     [9,   9,   2,    3,  9,   9],   # 1 sign
                     [8,   9,   2,    4,  5,   9],   # 2 digit
                     [9,   9,   4,    9,  9,   9],   # 3 dot
                     [8,   9,   4,    9,  5,   9],   # 4 number
                     [9,   6,   7,    9,  9,   9],   # 5 e
                     [9,   9,   7,    9,  9,   9],   # 6 e sign
                     [8,   9,   7,    9,  9,   9],   # 7 e digit
                     [8,   9,   9,    9,  9,   9],   # 8 success
                     [9,   9,   9,    9,  9,   9]    # 9 fail
        ]
        def char_to_input(c):
            if c in string.whitespace: return 0
            if c in '+-': return 1
            if c in '0123456789': return 2
            if c == '.': return 3
            if c == 'e': return 4
            return 5
        
        state = 0
        for c in s:
            inp = char_to_input(c)
            state = Delta[state][inp] 
            if state == 9: return False
        state = Delta[state][0]
        return state == 8