/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isValidSequence(TreeNode* root, vector<int>& arr) {
        stack<pair<TreeNode*, int>> tour;
        tour.push({root, 0});
        while (not tour.empty()) {
            auto pair = tour.top(); tour.pop();
            TreeNode* node = pair.first;
            int i = pair.second;
            if (node->val != arr[i]) continue;
            if (i == arr.size() - 1) {
                if (not(node->left or node->right)) return true;   
            } else {
                if (node->left) tour.push({node->left, i+1});
                if (node->right) tour.push({node->right, i+1});
            }
        }
        return false;
    }
};