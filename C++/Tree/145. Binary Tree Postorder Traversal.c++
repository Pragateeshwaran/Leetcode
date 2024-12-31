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

// class Solution {
// public:
//     void dfs(TreeNode* root, vector<int>& Array) {
//         if (!root) return;
//         dfs(root->left, Array);     // Traverse the left subtree
//         dfs(root->right, Array);    // Traverse the right subtree
//         Array.push_back(root->val); // Visit the current node
//     }
    
//     vector<int> postorderTraversal(TreeNode* root) {
//         vector<int> Result;
//         dfs(root, Result);
//         return Result;
//     }
// };

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        
    }
};

// Function to create a sample binary tree for testing
TreeNode* createSampleTree() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    return root;
}

// Main function for testing
int main() {
    Solution solution;
    TreeNode* root = createSampleTree();
    
    vector<int> result = solution.postorderTraversal(root);
    cout << "Postorder Traversal: ";
    for (int val : result) {
        cout << val << " ";
    }
    cout << endl;

    // Cleanup allocated memory
    delete root->left->left;
    delete root->left->right;
    delete root->left;
    delete root->right;
    delete root;
    
    return 0;
}
