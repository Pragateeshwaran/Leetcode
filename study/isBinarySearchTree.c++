#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node(int val) {
        this->val = val;
        left = nullptr;
        right = nullptr;
    }
};

bool isBSTUtil(Node* root, int& prev) {
    if (!root)
        return true;

    // In-order traversal: left
    if (!isBSTUtil(root->left, prev))
        return false;

    // Check current node value with previous
    if (root->val <= prev)
        return false;

    // Update prev to current node's value
    prev = root->val;

    // In-order traversal: right
    return isBSTUtil(root->right, prev);
}

bool isBST(Node* root) {
    int prev = INT_MIN;
    return isBSTUtil(root, prev);
}

int main() {
    Node* root = new Node(10);
    root->left = new Node(5);
    root->right = new Node(1);
    root->left->left = new Node(3);
    root->left->right = new Node(7);
    root->right->right = new Node(20);

    cout << isBST(root);  // Outputs 1 if BST, 0 otherwise
}
