class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        unordered_map<int, int> nd_party;
        for (int i=0;i<graph.size();i++){
            if (graph[i].empty() or nd_party.count(i)) continue;
            nd_party[i] = 0;
            deque<int> tour = {i};
            while (!tour.empty()) {
                int nd = tour.front(); tour.pop_front();  // bfs
                // int nd = tour.back(); tour.pop_back();  // dfs
                int party = nd_party[nd];
                for (int nei:graph[nd]) {
                    if (!nd_party.count(nei)) {
                        nd_party[nei] = 1-party;
                        tour.push_back(nei);
                    }
                    if (nd_party[nei]==party) return false;
                }
            }
        }
        return true;
    }
};