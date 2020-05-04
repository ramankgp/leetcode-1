class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> char_freq;
        for (char c: magazine) char_freq[c]++;
        for (char c: ransomNote) {
            if (not char_freq.count(c) or not char_freq[c]) return false;
            char_freq[c]--;
        }
        return true;
    }
};