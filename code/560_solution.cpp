// accum[i] = sum(array[0:i))
// sub of subarray [i,j] = accum[j] - accum[i-1]

// accum[j], k 
// count(i) such that i < j and accum[j] - accum[i] = k 
// count(i) = number of subarrays sum to k which ends at location j

// accum
// sum_amount: cnt_of_i


class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int accum = 0, count = 0;
        unordered_map<int, int> memo = {{0, 1}};
        for (int num: nums) {
            accum += num;
            count += memo[accum - k];
            memo[accum] = memo[accum] + 1;
        }
        return count;
    }
};