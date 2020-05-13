// apply bit count per number O(num*32)
// 000
// 001
// 010
// 011
// 100    
    
// num_bits[i] = num_bits[i & (i -1)] + 1


class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> bitCounts (num+1);
        for (int i=1;i<=num;i++){
            bitCounts[i] = bitCounts[i & (i -1)] + 1;
        }
        return bitCounts;
    }
};