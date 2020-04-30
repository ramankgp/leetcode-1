#    root
#    |  |
#    b  d
#    |  |
#    a  a
#    |  |
#    d* d*

# N = length of word
# Insert O(N) T/S
# Search with out . O(N)~T O(1)~S
# Search with . O(#total nodes in DS)~T O(#total nodes in DS)~S

class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.childrens = collections.defaultdict(WordDictionary.TrieNode)
            self.terminal = False
    
    def __init__(self):
        """ Initialize your data structure here."""
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        """ Adds a word into the data structure. """
        node = self.root
        for char in word:
            node = node.childrens[char]
        node.terminal = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. 
        A word could contain the dot character '.' to represent any one letter.
        """
        n = len(word)
        
        def find(node, i):
            if i == n: return node.terminal
            char = word[i]
            if char == '.':
                for key in node.childrens:
                    if find(node.childrens[key], i+1): 
                        return True
                return False
            elif char not in node.childrens:
                return False
            else:
                return find(node.childrens[char], i+1)
            
        return find(self.root, 0)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)