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
    int rangeSumBST(TreeNode* root, int L, int R) {
        if (not root) return 0;
        int total = 0;
        stack<TreeNode*> nodes;
        nodes.push(root);
        while (not nodes.empty()) {
            TreeNode* node = nodes.top(); nodes.pop();
            if (L<=node->val and node->val<=R) total += node->val;
            if (node->left and node->val>L) nodes.push(node->left);
            if (node->right and node->val<R) nodes.push(node->right);
        }
        return total;
    }
};