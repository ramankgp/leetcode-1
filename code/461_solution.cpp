// log_2^(max(x,y))

// 6 0110
// 5 0101
//     ^^
//     11
// dist = 2

// 6 ^ 5 0011
    
class Solution {
public:
    int hammingDistance(int x, int y) {
        int diff = x ^ y, dist = 0;
        while (diff){
            diff &= diff - 1;
            dist ++;
        }
        return dist;
    }
};