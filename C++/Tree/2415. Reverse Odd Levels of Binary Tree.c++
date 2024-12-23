#include <iostream>
#include <queue>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* reverseOddLevels(TreeNode* root) {
        traverseDFS(root->left, root->right, 0);
        return root;
    }

private:
    void traverseDFS(TreeNode* leftChild, TreeNode* rightChild, int level) {
        if (leftChild == nullptr || rightChild == nullptr) {
            return;
        }
        // If the current level is odd, swap the values of the children.
        if (level % 2 == 0) {
            int temp = leftChild->val;
            leftChild->val = rightChild->val;
            rightChild->val = temp;
        }

        traverseDFS(leftChild->left, rightChild->right, level + 1);
        traverseDFS(leftChild->right, rightChild->left, level + 1);
    }
};

// Function to create a binary tree from a vector of values.
TreeNode* createTree(const vector<int>& values) {
    if (values.empty()) return nullptr;

    TreeNode* root = new TreeNode(values[0]);
    queue<TreeNode*> q;
    q.push(root);

    int i = 1;
    while (!q.empty() && i < values.size()) {
        TreeNode* current = q.front();
        q.pop();

        if (i < values.size() && values[i] != -1) { // -1 represents null
            current->left = new TreeNode(values[i]);
            q.push(current->left);
        }
        i++;

        if (i < values.size() && values[i] != -1) {
            current->right = new TreeNode(values[i]);
            q.push(current->right);
        }
        i++;
    }

    return root;
}

// Function to print the binary tree level by level.
void printTree(TreeNode* root) {
    if (!root) return;

    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int levelSize = q.size();
        for (int i = 0; i < levelSize; ++i) {
            TreeNode* current = q.front();
            q.pop();
            if (current) {
                cout << current->val << " ";
                q.push(current->left);
                q.push(current->right);
            } else {
                cout << "null ";
            }
        }
        cout << endl;
    }
}

int main() {
    // Example tree: [2, 3, 5, 8, 13, 21, 34]
    // Tree structure:
    //        2
    //      /   \
    //     3     5
    //    / \   / \
    //   8  13 21 34

    vector<int> values = {2, 3, 5, 8, 13, 21, 34};
    TreeNode* root = createTree(values);

    cout << "Original Tree:" << endl;
    printTree(root);

    Solution solution;
    solution.reverseOddLevels(root);

    cout << "Tree after reversing odd levels:" << endl;
    printTree(root);

    return 0;
}
