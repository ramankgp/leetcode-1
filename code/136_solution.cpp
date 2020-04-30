// 0 ^ x = x
// x ^ x = 0
// (a ^ b) ^ c = a ^ (b ^ c)


class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (int num: nums) res ^= num;
        return res;
    }
};