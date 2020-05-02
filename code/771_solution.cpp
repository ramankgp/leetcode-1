class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int total = 0;
        unordered_set<char> jewels;
        for (char jewel: J) jewels.insert(jewel);
        // O(52N) O(1)
        // for (char stone: S) total += count(J.begin(), J.end(), stone);      
        // O(N) O(52)
        for (char stone: S) total += jewels.count(stone);        
        return total;
    }
};