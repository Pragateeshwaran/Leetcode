#include <iostream>
#include <vector>
#include <queue>
using namespace std;

/**
 * Definition for a binary tree node.
 */
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
    vector<double> averageOfLevels(TreeNode* root) {
        if (!root) return {}; // Return an empty vector if the tree is empty.

        vector<double> result;          // To store averages of each level.
        queue<TreeNode*> Q;             // Queue for level-order traversal.
        Q.push(root);                   // Start with the root node.

        while (!Q.empty()) {
            int size = Q.size();        // Number of nodes at the current level.
            double sum = 0;            // To calculate the sum of values at the current level.

            for (int i = 0; i < size; ++i) {
                TreeNode* node = Q.front(); // Get the front node in the queue.
                Q.pop();                     // Remove it from the queue.

                sum += node->val;            // Add its value to the sum.

                // Push its left and right children (if they exist) to the queue.
                if (node->left) Q.push(node->left);
                if (node->right) Q.push(node->right);
            }

            result.push_back(sum / size); // Calculate the average and add it to the result.
        }

        return result; // Return the averages for all levels.
    }
};

// Helper function to test the code.
int main() {
    // Creating a sample binary tree:
    //         3
    //        / \
    //       9  20
    //          /  \
    //         15   7
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20, new TreeNode(15), new TreeNode(7));

    Solution solution;
    vector<double> averages = solution.averageOfLevels(root);

    // Print the averages.
    cout << "Averages of each level: ";
    for (double avg : averages) {
        cout << avg << " ";
    }

    return 0;
}
