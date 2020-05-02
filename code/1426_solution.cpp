class Solution {
public:
    int countElements(vector<int>& arr) {
        int count = 0;
        // Time/Space O(N) 
        // unordered_map<int, int> table;
        // for (int num:arr) table[num] += 1;
        // for (auto kv: table) {
        //     if (table.find(kv.first + 1) != table.end()) {
        //         count += table[kv.first];
        //     }
        // }
        
        // Time O(NlogN) Space O(1)
        sort(arr.begin(), arr.end());
        int strike = 1;
        for (int i=1; i<arr.size(); i++) {
            if (arr[i] == arr[i-1] + 1) count += strike;
            strike = (arr[i] == arr[i-1]) ? strike + 1 : 1;
        }
        return count;
    }
};