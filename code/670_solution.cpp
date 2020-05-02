class Solution {
public:
    int maximumSwap(int num) {
        int max_digit=-1, max_loc=-1, l_digit=-1, l_loc, r_digit, r_loc;
        for (int loc=0,n=num;n;n/=10,loc++){
            int curr_digit = n % 10;
            if (curr_digit > max_digit) {
                max_digit = curr_digit;
                max_loc = loc;
            } else if (curr_digit < max_digit) {
                l_digit = curr_digit;
                l_loc = loc;
                r_digit = max_digit;
                r_loc = max_loc;
            }
        }
        if (l_digit == -1) return num;
        else return num + (r_digit - l_digit) * (int)(pow(10, l_loc) - pow(10, r_loc));
    }
};