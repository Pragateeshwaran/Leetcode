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
    int find_index(vector<int>& inorder, int val) {
        for (int i = 0; i < inorder.size(); i++) {
            if (inorder[i] == val) {
                return i;
            }
        }
        return -1; // Return -1 instead of -111 for clarity
    }

    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (inorder.empty() || postorder.empty()) {
            return nullptr;
        }

        // Last element in postorder is the root
        int root_val = postorder.back();
        TreeNode* root = new TreeNode(root_val);
        postorder.pop_back(); // Remove the last element from postorder

        // Find index of root in inorder
        int mid = find_index(inorder, root_val);

        // Construct left and right subtree inorder vectors
        vector<int> inorder_left(inorder.begin(), inorder.begin() + mid);
        vector<int> inorder_right(inorder.begin() + mid + 1, inorder.end());

        // Construct left and right subtree postorder vectors
        vector<int> postorder_left(postorder.begin(), postorder.begin() + inorder_left.size());
        vector<int> postorder_right(postorder.begin() + inorder_left.size(), postorder.end());

        // Recursively build left and right subtrees
        root->left = buildTree(inorder_left, postorder_left);
        root->right = buildTree(inorder_right, postorder_right);

        return root;
    }
};