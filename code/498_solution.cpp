// let d = 1 mean up-right -1 be bottom-left
// at r, c
//     // direction up-right    nr, nc = r-1, c+1
//     // direction bottom-left nr, nc = r+1, c-1
//     d = 1 nr, nc = r-d, c+d
//     d =-1 nr, nc = r-d, c+d    
    
// hit wall
//     d = 1 if we can't go right we go down
//     d =-1 if we can't go down we go right

class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        if (matrix.empty()) return {};
        int M=matrix.size(), N=matrix[0].size();
        int r=0, c=0, d=1;
        vector<int> res;
        while (res.size() != M*N) {
            res.push_back(matrix[r][c]);
            int nr=r-d, nc=c+d;
            bool outBound = (nr < 0 or nr == M or nc < 0 or nc == N);
            if (outBound) {
                if (d==1) {
                    if (nc==N) r++;
                    else c++;
                } else {
                    if (nr==M) c++;
                    else r++;                    
                }
                d = -d;
            } else {
                r = nr;
                c = nc;
            }
        }
        return res;
    }
};
