class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        for (int l=0, r=0; r<nums.size(); r++){
            if (nums[r]) {
                swap(nums[r], nums[l]);
                l++;
            }
        }
    }
};