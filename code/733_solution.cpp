// sr = 1, sc = 1, newColor = 2
// oldColor = 1
// [
//     [2,2,2],
//     [2,2,0],
//     [2,0,1]
// ]

// [
//     [1,1,1],
//     [1,1,0],
//     [1,0,1]
// ]

class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int nrow = image.size(), ncol = image[0].size();
        int oldColor = image[sr][sc];
        if (oldColor == newColor) return image;
        
        deque<pair<int, int>> toFill;
        toFill.push_back({sr, sc});
        while (not toFill.empty()){
            // bfs
            auto loc = toFill.front();
            toFill.pop_front();
            // dfs
            // auto loc = toFill.back();
            // toFill.pop_back();
            int row = loc.first, col = loc.second;
            image[row][col] = newColor;
            if (row-1 >= 0 and image[row-1][col] == oldColor) toFill.push_back({row-1, col});
            if (row+1 < nrow and image[row+1][col] == oldColor) toFill.push_back({row+1, col});
            if (col-1 >= 0 and image[row][col-1] == oldColor) toFill.push_back({row, col-1});
            if (col+1 < ncol and image[row][col+1] == oldColor) toFill.push_back({row, col+1});
        }
        return image;
    }
};