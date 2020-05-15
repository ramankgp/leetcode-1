//                         res^=x res^=x res^=y res^z res^z
//                 initial first second third   fourth fifth
// 1/2 res ith pos 0       1     0      1       0      1

//                            x     x      x     z      z     z     y
//                    initial first second third fourth fifth sixth sevnth
// 1/3 first ith pos  0       1     0      0     1      0     0     1
// 2/3 second ith pos 0       0     1      0     0      1     0     0

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        // int first[32]={0}, second[32]={0};
        // for (int num:nums){
        //     for (int i=0;i<32;i++){
        //         int bit = (num >> i) & 1;
        //         // if (bit) {
        //             // if (first[i]==0 and second[i]==0){
        //             //     first[i]=1;
        //             // } else if (first[i] and second[i]==0) {
        //             //     first[i]=0; 
        //             //     second[i]=1;
        //             // } else if (first[i] == 0 and second[i]){
        //             //     second[i]=0;  
        //             // } 
        //         // }
        //         if (bit & (second[i]^bit)) first[i]^=bit;
        //         if (bit & (first[i]^bit)) second[i]^=bit;
        //     }
        // }
        // int result=0;
        // for (int i=0;i<31;i++){
        //     if (first[i]^first[31]) result += 1 << i;
        // }
        // return first[31] ? ~result : result; 
        // for (int i=0;i<32;i++) result |= first[i] << i;
        // return result;
                
        int first=0, second=0;
        for (int num:nums){
            first = ~second & (first ^ num);
            second =  ~first & (second ^ num);
        }
        return first;
    }
};