// a, b, a ^(xor) b
// 1  1  0
// 1  0  1
// 0  0  0
// 0  1  1

// b ^ 1 -> compliment of b    

//   1011
// ^    1
// -------
//   1010

// 1 << 1 = 10      
      
//   1010
// ^   10 
// -------
//   1000      

//  1011 >> 1 101 >> 1 10 >> 1 1 >> 0     
      
//   1011
// ^ 1111  = 10000 - 1 = 1111
// -------
//   1010

class Solution {
public:
    int findComplement(int num) {
        if (num==0) return 1;
        int num_comp = num;
        for (int i=0;num;num>>=1,i++) num_comp ^= 1 << i;
        return num_comp;
    }
};