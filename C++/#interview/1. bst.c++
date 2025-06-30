#include<iostream>
using namespace std;

struct Node{
    int data;
    Node* left;
    Node* right;
    Node(int val) : data(val), left(nullptr), right(nullptr) {}
};

Node* root = nullptr;

Node* insert(Node* root, int val) {
    if (root == nullptr) {
        root = new Node(val);
        return root;
    }

    if (val < root->data) {
        root->left = insert(root->left, val);
    } else if (val > root->data) {
        root->right = insert(root->right, val);
    } 
    return root;
}

int height(Node* root){
    if(!root){
        return 0;
    }
    int lheight = height(root->left);
    int rheight = height(root->right);
    return max(lheight, rheight) + 1;
}

int inorder(Node* root) {
    if (root == nullptr) {
        return 0;
    }
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
    return 0;
}   


int main(){
    int arr[] = {9, 5, 3, 4, 2, 6, 23, 45, 0};
    int n = sizeof(arr) / sizeof(arr[0]);
    for (int i = 0; i < n; i++) {
        root = insert(root, arr[i]);
    }
    cout << "Binary Search Tree created successfully." << endl;
    inorder(root);
    cout << endl;
    cout << "The Tree's height is:  " << height(root)<<endl;
    return 0;
}

    
