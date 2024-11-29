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
    bool isSymmetric(TreeNode* root) {
        if (!root) return true; // A null tree is symmetric
        return dfs(root->left, root->right); // Check symmetry between left and right subtrees
    }
    
    bool dfs(TreeNode* rootl, TreeNode* rootr) {
        if (!rootl && !rootr) 
            return true; // Both subtrees are null, so they are symmetric
        if (!rootl || !rootr) 
            return false; // One subtree is null, the other is not, so not symmetric
        // Check if values are equal and subtrees are symmetric
        return (rootl->val == rootr->val) &&
               dfs(rootl->left, rootr->right) &&
               dfs(rootl->right, rootr->left);
    }
};

// Helper function to create a tree
TreeNode* createTree() {
    // Example: Create a symmetric tree manually
    //         1
    //       /   \
    //      2     2
    //     / \   / \
    //    3   4 4   3

    TreeNode* node1 = new TreeNode(1);
    TreeNode* node2_left = new TreeNode(2);
    TreeNode* node2_right = new TreeNode(2);
    TreeNode* node3_left = new TreeNode(3);
    TreeNode* node4_left = new TreeNode(4);
    TreeNode* node4_right = new TreeNode(4);
    TreeNode* node3_right = new TreeNode(3);

    node1->left = node2_left;
    node1->right = node2_right;

    node2_left->left = node3_left;
    node2_left->right = node4_left;

    node2_right->left = node4_right;
    node2_right->right = node3_right;

    return node1;
}

int main() {
    // Create the tree
    TreeNode* root = createTree();

    // Check if the tree is symmetric
    Solution solution;
    if (solution.isSymmetric(root)) {
        cout << "The tree is symmetric." << endl;
    } else {
        cout << "The tree is not symmetric." << endl;
    }

    // Free the allocated memory (optional but good practice)
    delete root->left->left;   // node3_left
    delete root->left->right;  // node4_left
    delete root->right->left;  // node4_right
    delete root->right->right; // node3_right
    delete root->left;         // node2_left
    delete root->right;        // node2_right
    delete root;               // node1

    return 0;
}
