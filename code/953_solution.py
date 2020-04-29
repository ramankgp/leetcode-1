class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {letter: idx for idx, letter in enumerate(order)}
        
        def lex_order(w1, w2):
            for c1, c2 in zip(w1, w2):
                if order[c1] < order[c2]: return True
                if order[c1] > order[c2]: return False
            return len(w1) <= len(w2)
        
        for w1, w2 in zip(words, words[1:]):
            if not lex_order(w1, w2): return False
        return True