// 6  0110
// 5  0101
// 4  0100
// 3  0011
// 10 1010    
//       ^
//       6=2x3
//      ^
//      6=2x3
//    ^
//    4=1x4

// Time O(32*N) 
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        int total_dist=0;
        for (int i=0; i<32; i++){
            int ones = 0;
            for (int num: nums) ones += (num >> i) & 1;
            total_dist += ones * (nums.size() - ones);
        }
        return total_dist;
    }
};