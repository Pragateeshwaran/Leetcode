#include <iostream>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root) 
            return 0; // Base case: if the tree is empty, depth is 0
        return dfs(root);
    }

    int dfs(TreeNode* root) {
        if (!root) 
            return 0; // Base case: null node has depth 0
        // Recursively calculate depth of left and right subtrees
        int leftDepth = dfs(root->left);
        int rightDepth = dfs(root->right);
        // Return the maximum of left and right depths, plus 1 for the current node
        return 1 + max(leftDepth, rightDepth);
    }

    int max(int a, int b) {
        return a > b ? a : b; // Helper function for finding the maximum of two numbers
    }
};

// Helper function to create a sample tree
TreeNode* createTree() {
    // Example: Create a tree manually
    //         1
    //       /   \
    //      2     3
    //     / \
    //    4   5
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    return root;
}

int main() {
    // Create the tree
    TreeNode* root = createTree();

    // Find the maximum depth
    Solution solution;
    cout << "The maximum depth of the tree is: " << solution.maxDepth(root) << endl;

    // Free allocated memory (optional but good practice)
    delete root->left->left;   // Node 4
    delete root->left->right;  // Node 5
    delete root->left;         // Node 2
    delete root->right;        // Node 3
    delete root;               // Root node

    return 0;
}
