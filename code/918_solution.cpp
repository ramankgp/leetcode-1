// accum[i] = sum(A[:i])

// accum[b]-accum[a] = sum(A[:b]) - sum(A[:a]) = sum(A[a:b])

    
// if sum(A[c:b]) is the maximum circular(meaning b < c) subarray sum 
// then b = argmax_i{accum[i]} and c = argmin_i{accum[i]}.

    
//          b
//         /\
//        /  \
// s   /\/    \
// \  /        \/\      e
//  \/            \    /
//   a             \  /
//                  \/
//                   c
// ------------------------> i    



class Solution {
public:
    int maxSubarraySumCircular(vector<int>& A) {
        int total=0,curr_min=0,curr_max=0,min_sum=INT_MAX,max_sum=INT_MIN;
        for (int num:A) {
            total += num;
            curr_max = max(curr_max+num, num);
            curr_min = min(curr_min+num, num);
            max_sum = max(max_sum, curr_max);
            min_sum = min(min_sum, curr_min);
        }
        return max_sum < 0 ? max_sum : max(max_sum, total-min_sum);
    }
};