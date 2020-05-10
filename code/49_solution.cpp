class Solution {
public:
    // -> NklogK
    string hash(string str) {
        sort(str.begin(), str.end());
        return str;
    }
    
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> group_by;
        vector<vector<string>> anagrams;
        for (auto str: strs) group_by[hash(str)].push_back(str);
        for (auto group: group_by) anagrams.push_back(group.second);
        return anagrams;
    }
};
