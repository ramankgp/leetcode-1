// 123 -> 132 -> 213 -> 231 -> 312 -> 321
//  ^                                  |
//  |----------------------------------|   

// 12345 - 12354

// 123|54 - swap 3 4 - 124|53 - reverse 5 3 - 124|35 
    
// 314|52 - swap 4 5 - 315|42 - reverse 4 2 - 315|24

// 31|542 - swap 1 2 - 32|541 - reverse 5 4 1 - 32|145    
    
// 54321 - 12345    
    
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int l = nums.size() - 2;
        while (l>=0 and nums[l]>=nums[l+1]) l--;
        if (l>=0) {
            int r = nums.size() - 1;
            while (nums[r] <= nums[l]) r--;
            swap(nums[l], nums[r]);
        }
        reverse(nums.begin()+l+1, nums.end());
    }
};