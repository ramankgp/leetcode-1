// find i and j such that sum(arr[i:j)) % k = 0

// accum[i] = sum(arr[0:i))
// sum(arr[i:j)) = accum[j] - accum[i]             

// accum[j] = nj = a*k+b where a, b = divmod(nj, k)
// accum[i] = ni = c*k+d where c, d = divmod(ni, k)
// where 0<= b,d < k    
// sum(arr[i:j)) = accum[j] - accum[i] = (a-c) * k + (b - d)
// we want that b = d        
        
// instead of accum[i] what we really want is: 
        
// r[i] = sum(arr[0:i)) % k    
// sum(arr[i:j)) is a mutilpe of k if r[j] = r[i]

// cahche [sum(arr[0:i)) % k] -> i


class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> m = {{0,-1}};
        int r=0;
        for (int i=0; i<nums.size();i++){
            r += nums[i];
            if (k) r %= k;
            if (m.count(r)) {
                if (i - m[r] > 1) return true;
            }
            else {
                m[r] = i;
            }
        }
        return false;
    }
};