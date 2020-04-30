// f(i,j) = minimal path sum from (0,0) to (i,j)
// f(i,j) = min(f(i-1,j), f(i,j-1)) + grid[i][j]
// want to return f(m-1, n-1)
// [
//   [1,4,5],
//   [2,7,6],
//   [6,0,0]
// ]

// [1,4,5]
// [2,7,6]
// [6,8,7]

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m=grid.size(), n=grid[0].size();
// // 2D O(MN) T O(MN) S        
//         int dp[m][n];
//         dp[0][0] = grid[0][0];
//         for (int r=1;r<m;r++) dp[r][0] = dp[r-1][0] + grid[r][0];
//         for (int c=1;c<n;c++) dp[0][c] = dp[0][c-1] + grid[0][c];
        
//         for (int r=1;r<m;r++) {
//             for (int c=1;c<n;c++) {
//                 dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1]);
//             }
//         }
//         return dp[m-1][n-1];

        // // 1D O(MN) T O(N) S        
        int dp[n];
        dp[0] = grid[0][0];
        for (int c=1;c<n;c++) dp[c] = dp[c-1] + grid[0][c];
        for (int r=1;r<m;r++) {
            for (int c=0;c<n;c++){
                if (c==0) dp[c] += grid[r][c];
                else dp[c] = grid[r][c] + min(dp[c], dp[c-1]);
            }
        }
        return dp[n-1];
    }
};