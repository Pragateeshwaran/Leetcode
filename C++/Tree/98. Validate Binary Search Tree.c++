#include <iostream>
#include <climits>

// TreeNode structure as defined
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

// Solution class with isValidBST method
class Solution {
public:
    bool dfs(TreeNode* root, long long upper_bound, long long lower_bound) {
        if (!root) {
            return true;
        }
        if (root->val <= lower_bound || root->val >= upper_bound) {
            return false;
        }
        return dfs(root->left, root->val, lower_bound) && dfs(root->right, upper_bound, root->val);
    }

    bool isValidBST(TreeNode* root) {
        if (!root) {
            return true;
        }
        long long positive = (long long)INT_MAX + 1;
        long long negative = (long long)INT_MIN - 1;
        return dfs(root, positive, negative);
    }
};

int main() {
    // Constructing the tree from the example input
    TreeNode* root = new TreeNode(2147483644);
    root->left = new TreeNode(-2147483648);
    root->right = new TreeNode(2147483646);
    root->right->left = new TreeNode(2147483645);
    root->right->right = new TreeNode(2147483647);

    Solution sol;
    std::cout << (sol.isValidBST(root) ? "True" : "False") << std::endl;

    return 0;
}
