#include <iostream>
#include <vector>
#include <stack>
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
//         Array.push_back(root->val);  // Visit the current node
//         dfs(root->left, Array);     // Traverse the left subtree
//         dfs(root->right, Array);    // Traverse the right subtree
//     }
    
//     vector<int> preorderTraversal(TreeNode* root) {
//         vector<int> Result;
//         dfs(root, Result);
//         return Result;
//     }
// };

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        stack<TreeNode*> stacks;
        vector<int>result;
        while(root!=nullptr || not stacks.empty()){
            while(root!=nullptr){
                result.push_back(root->val);
                stacks.push(root);
                root = root->left;
            }
            root = stacks.top();
            stacks.pop();
            root = root->right;
            
        }
        return result;
    }
};

// Function to create a sample binary tree for testing
TreeNode* createSampleTree() {
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);
    return root;
}

// Main function for testing
int main() {
    Solution solution;
    TreeNode* root = createSampleTree();
    
    vector<int> result = solution.preorderTraversal(root);
    cout << "Preorder Traversal: ";
    for (int val : result) {
        cout << val << " ";
    }
    cout << endl;

    // Cleanup allocated memory
    delete root->right->left;
    delete root->right;
    delete root;
    
    return 0;
}
