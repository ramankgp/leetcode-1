// Counter(arr[i:j)) -> {0:a, 1:b}  want a==b
// Counter(arr[i:j)) = Counter(arr[0:j)) - Counter(arr[0:i)) 
                                                    
// Counter(arr[0:j)) = {0:a, 1:b}
// Counter(arr[0:i)) = {0:c, 1:d}            
// Counter(arr[0:j)) - Counter(arr[0:i)) = {0:(a-c), 1:(b-d)}                                           
// want (a-c) = (b-d) == (a-b) = (c-d) = diff in #0 and #1 in the window

// c[i] = #0-#1

// m[#0-#1] = 1


class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> m = {{0,-1}}; //O(N) in space
        int diff=0, max_len=0;
        for (int i=0; i<nums.size(); i++){ //O(N) in time
            diff += (nums[i]) ? 1 : -1;
            if (m.count(diff)) max_len = max(max_len, i-m[diff]);
            else m[diff] = i;
        }
        return max_len;
    }
}; 