class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend==INT_MIN and divisor==-1) return INT_MAX;
        if (dividend==INT_MIN and divisor==1) return INT_MIN;
        
        bool negative = (dividend < 0) ^ (divisor < 0);
        dividend = dividend > 0 ? -dividend : dividend;
        divisor = divisor > 0 ? -divisor : divisor;
        
        // 63 / 2, 4, 8, 16, 32,
        int quotient = 0;
        // while (dividend <= divisor) { // O(N)
        //     dividend -= divisor;
        //     quotient++;
        // }
        
        // O((logN)^2)
        // while (dividend <= divisor) { // O(logN)
        //     int i=1, accum=divisor;
        //     while (accum>INT_MIN>>1 and dividend<=accum+accum) {
        //         i += i;
        //         accum += accum;
        //     }
        //     dividend -= accum;
        //     quotient += i;
        // }
        
        // O(logN)
        int i=1, accum=divisor;
        while (accum>=INT_MIN>>1 and dividend<=accum+accum) {
            i <<= 1;
            accum += accum;
        }
        while (dividend <= divisor) {
            if (dividend <= accum){
                dividend -= accum;
                quotient += i;
            }
            accum >>= 1; // O(32)
            i >>= 1;
        }
        
        return negative ? -quotient : quotient;
    }
};