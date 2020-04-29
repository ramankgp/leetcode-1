class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = set('aeiouAEIOU')
        
        def tranform(word, i):
            if word[0] not in vowel:
                word = word[1:] + word[0]
            return word + 'ma' + 'a' * i
        
        return ' '.join(tranform(word, i) for i, word in enumerate(S.split(), 1))