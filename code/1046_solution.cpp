class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq(stones.begin(), stones.end());
        while (pq.size() > 1){
            int w1 = pq.top(); pq.pop();
            int w2 = pq.top(); pq.pop();
            if (w1 != w2) pq.push(w1 - w2);
        }
        return pq.empty() ? 0 : pq.top();
    }
};