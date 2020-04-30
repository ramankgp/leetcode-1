// 9 -> 81
// 99 -> 162
// 999 -> 243
// 9999 -> 3xx
// n = xxxxxx - > 81 * log_10^n -> log(n) in time

class Solution {
public:
    int simulate(int num) {
        int res;
        for (res=0;num;num/=10) {
            res += (num%10) * (num%10);
        }
        return res;
    }
    
    bool isHappy(int n) {
        unordered_set<int> seen;
        seen.insert(n);
        while (n != 1) {
            n = simulate(n);
            if (seen.find(n) == seen.end()) {
                seen.insert(n);       
            } else {
                return false;
            }
        }
        return true;
    }
};