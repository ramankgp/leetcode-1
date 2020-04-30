class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) return {};
        vector<vector<int>> merged;
        sort(intervals.begin(), intervals.end());
        int l = intervals[0][0], r = intervals[0][1];
        for (auto interval:intervals){
            if (interval[0] > r) {
                merged.push_back({l,r});
                l = interval[0];
                r = interval[1];
            } else {
                r = max(r, interval[1]);
            }
        }
        merged.push_back({l,r});
        return merged;
    }
};