  //   root
  //     |
  // --------      
  // |      |
  // a(F)   d(F)
  // |      |
  // p      o(F)
  // |      |
  // p(T)   g(T)
  // |
  // l
  // |
  // e(T)

class TrieNode {
private:
    bool flag;
    unordered_map<char, TrieNode*> children;
public:
    TrieNode() {flag=false;children={};}
    bool get_flag(){return flag;}
    void set_flag(){flag=true;}
    bool contains(char c){return children.count(c) > 0;}
    void set_child(char c, TrieNode* node){children[c]=node;}
    TrieNode* get_child(char c){return children[c];}
};

class Trie {
private:
    TrieNode* root;
public:
    /** Initialize your data structure here. */
    Trie() {root = new TrieNode();}
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode* node = root;
        for (char c:word){
            if (not node->contains(c)) node->set_child(c, new TrieNode());
            node = node->get_child(c);
        }
        node->set_flag();
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        TrieNode* node = root;
        for (char c:word){
            if (not node->contains(c)) return false;
            node = node->get_child(c);
        }
        return node->get_flag();
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        TrieNode* node = root;
        for (char c:prefix){
            if (not node->contains(c)) return false;
            node = node->get_child(c);
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */