#include <vector>
#include 
using namespace std;

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
    // Helper function to find the index of a value in the inorder array
    int find_index(int val, const vector<int>& inorder) {
        for (int i = 0; i < inorder.size(); i++) {
            if (inorder[i] == val) {
                return i;
            }
        }
        return -1;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        // Base case: If either array is empty, return nullptr
        if (preorder.empty() || inorder.empty()) {
            return nullptr;
        }

        // Root is the first element in preorder
        int root_val = preorder[0];
        TreeNode* root = new TreeNode(root_val);

        // Find the index of the root in inorder
        int mid = find_index(root_val, inorder);

        // Build the left subtree using slices of preorder and inorder
        vector<int> left_preorder(preorder.begin() + 1, preorder.begin() + 1 + mid);
        vector<int> left_inorder(inorder.begin(), inorder.begin() + mid);
        root->left = buildTree(left_preorder, left_inorder);

        // Build the right subtree using slices of preorder and inorder
        vector<int> right_preorder(preorder.begin() + 1 + mid, preorder.end());
        vector<int> right_inorder(inorder.begin() + mid + 1, inorder.end());
        root->right = buildTree(right_preorder, right_inorder);

        return root;
    }
};
