#include <iostream>
#include <vector>
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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        inorderHelper(root, result);
        return result;
    }

private:
    void inorderHelper(TreeNode* node, vector<int>& result) {
        if (node == nullptr) return;
        inorderHelper(node->left, result);   // Visit left subtree
        result.push_back(node->val);        // Visit current node
        inorderHelper(node->right, result); // Visit right subtree
    }
};

// Helper function to create a binary tree
TreeNode* createTree() {
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);
    return root;
}

int main() {
    Solution solution;

    // Create a sample tree
    TreeNode* root = createTree();

    // Perform in-order traversal
    vector<int> result = solution.inorderTraversal(root);

    // Print the result
    cout << "In-order Traversal: ";
    for (int val : result) {
        cout << val << " ";
    }
    cout << endl;
    return 0;
}
