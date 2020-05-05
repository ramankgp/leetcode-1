// 11 10 01 00

class Solution {
public:
    bool isMonotonic(vector<int>& A) {
        int asc=1,dsc=1;
        for (int i=0;i<A.size()-1;i++){
            if (A[i+1] > A[i]) dsc=0;
            if (A[i+1] < A[i]) asc=0;
        }
        return asc or dsc;
    }
};