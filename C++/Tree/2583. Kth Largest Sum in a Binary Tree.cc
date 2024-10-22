#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int kthLargestLevelSum(TreeNode* root, int k) {
        if (!root) return -1;

        queue<TreeNode*> q;
        q.push(root);
        vector<int> level_sums;

        while (!q.empty()) {
            int nodes_len = q.size();
            int sums = 0;

            for (int i = 0; i < nodes_len; ++i) {
                TreeNode* node = q.front();
                q.pop();
                sums += node->val;

                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }

            level_sums.push_back(sums);
        }

        sort(level_sums.begin(), level_sums.end(), greater<int>());

        return k <= level_sums.size() ? level_sums[k - 1] : -1;
    }
};

int main() {
    // Creating the binary tree
    TreeNode* root = new TreeNode(5);
    root->left = new TreeNode(3);
    root->right = new TreeNode(8);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(4);
    root->right->left = new TreeNode(7);
    root->right->right = new TreeNode(9);

    // Solution instance
    Solution solution;
    int k = 2;

    // Output the result
    cout << "K-th largest level sum: " << solution.kthLargestLevelSum(root, k) << endl;

    // Free memory
    delete root->left->left;
    delete root->left->right;
    delete root->right->left;
    delete root->right->right;
    delete root->left;
    delete root->right;
    delete root;

    return 0;
}
