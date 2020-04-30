class Solution {
public:
    bool checkValidString(string s) {
        int max_open=0, min_open=0;
        for (char c:s) {
            max_open = c==')' ? max_open-1 : max_open+1;
            min_open = c=='(' ? min_open+1 : max(min_open-1, 0);
            // if (c=='(') {
            //     max_open++;
            //     min_open++;
            // }
            // if (c==')') {
            //     max_open--;
            //     min_open = max(min_open-1, 0);
            // }
            // if (c=='*') {
            //     max_open++;
            //     min_open = max(min_open-1, 0);
            // }
            if (max_open < 0) return false;
        }
        return min_open == 0;
    }
};