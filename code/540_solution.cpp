//  0 1 2 3 4  5  6  7 8
// [3,3,7,7,10,11,11,5,5]
//  1 1 1 1 2  3  3  3 3

// 1 2n, 2n+1
// 2 2n
// 3 2n-1, 2n

// m ^ 1

class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int l=0, h=nums.size()-1;
        while (l < h) {
            int m = l + (h - l) / 2;
            if (nums[m] == nums[m ^ 1]) l = m + 1;
            else h = m;
        }
        return nums[l];
    }
};