class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l=0, h=nums.size()-1, m;
        while (l<=h){
            m = (l+h)/2;
            if (nums[m] == target) return m;
            
            if (nums[m] >= nums[l]) {
                // left is sorted
                if (nums[l] <= target and target < nums[m]) h=m-1;
                else l=m+1;
            } else {
                // right is sorted
                if (nums[m] < target and target <= nums[h]) l=m+1;
                else h=m-1;
            }
        }
        return -1;
    }
};