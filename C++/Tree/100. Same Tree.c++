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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        return dfs(p, q);
    }
    
    bool dfs(TreeNode* p, TreeNode* q) {
        if (!p && !q) 
            return true; // Both nodes are null, so they are identical
        if (!p || !q) 
            return false; // One node is null, the other is not
        return (p->val == q->val) && // Check values
               dfs(p->left, q->left) && // Check left subtrees
               dfs(p->right, q->right); // Check right subtrees
    }
};

// Helper function to create a tree
TreeNode* createTree1() {
    // Create the first tree:
    //      1
    //     / \
    //    2   3
    TreeNode* node1 = new TreeNode(1);
    TreeNode* node2 = new TreeNode(2);
    TreeNode* node3 = new TreeNode(3);
    node1->left = node2;
    node1->right = node3;
    return node1;
}

TreeNode* createTree2() {
    // Create the second tree:
    //      1
    //     / \
    //    2   3
    TreeNode* node1 = new TreeNode(1);
    TreeNode* node2 = new TreeNode(2);
    TreeNode* node3 = new TreeNode(3);
    node1->left = node2;
    node1->right = node3;
    return node1;
}

int main() {
    // Create two trees
    TreeNode* tree1 = createTree1();
    TreeNode* tree2 = createTree2();

    // Compare the trees
    Solution solution;
    if (solution.isSameTree(tree1, tree2)) {
        cout << "The trees are identical." << endl;
    } else {
        cout << "The trees are not identical." << endl;
    }

    // Free memory (optional but recommended)
    delete tree1->left;   // node2
    delete tree1->right;  // node3
    delete tree1;         // root node

    delete tree2->left;   // node2
    delete tree2->right;  // node3
    delete tree2;         // root node

    return 0;
}
