class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int window_sum = nums[0];
        int max_sum = window_sum;
        for (int i = 1; i < nums.size(); i++) {
            int num = nums[i];
            window_sum = max(window_sum + num, num);
            max_sum = max(max_sum, window_sum);
        }
        return max_sum;
    }
};