// 3   011
// 5   101
// 3^5 110 
//      ^
// x & -x     
// if num & 010 ? goto [2,2,3] else goto [1,1,5]    
// 3^3^5 

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int diff = accumulate(nums.begin(), nums.end(), 0, bit_xor<int>());
        int mask = diff & -diff;
        int x=0, y=0;
        for (int num: nums){
            if (num & mask) x^=num;
            else y^=num;
        }
        return {x,y};
    }
};