#include<iostream>
#include<vector>
using namespace std;
struct Node{
    int val;
    Node* left;
    Node* right;
    Node(int val){
        this->val = val;
        this->left = nullptr;
        this->right = nullptr;
    }
};

Node* create(Node* root, int val){
    
    if(root == NULL){
        Node* nodes = new Node(val);
        root = nodes;
        return root;
    }
    if(val < root->val){
        root->left = create(root->left, val);
    }
    else{
        root->right = create(root->right, val);
    }
    return root;
}

void read(Node* root){
    if(root == NULL)
        return;
    read(root->left);
    cout<<root->val<<" ";
    read(root->right);
}

void update(Node* root, int val1, int val2){
    if(root == NULL)
        return;
    update(root->left, val1, val2);
    if(root->val == val1){
        root->val = val2;
    }
    update(root->right, val1, val2);
}

Node* delete_node(Node* node, int val){
    if(node == nullptr)
        return nullptr;
    if(node->val == val){
        if(node->left == nullptr and node->right == nullptr){
            delete node;
            return nullptr;
        }
        if(node->left and not node->right){
            node = node->left;
            return node;
        }
        if(node->right and not node->left){
            node = node->right;
            return node;
        }
        if(node->left and node->right){
            Node* temp = node->right;
            while(temp->left != nullptr){
                temp = temp->left;
            }
            node->val = temp->val;
            node->right = delete_node(node->right, temp->val);
            return node;
        }
        return node;
    }
    else{
        if(node->val > val){
            node->left = delete_node(node->left, val);
        }
        else{
            node->right = delete_node(node->right, val);
        }
    }
    return node;
}

int main(){
    Node* root = nullptr;
    vector<int> array = {11, 465 ,564, 4, 2, 7, 8, 9, 1, 0};
    for(int i=0; i<array.size(); i++){
        root = create(root, array[i]);
    }
    read(root);
    update(root, 11, 100);
    cout<<endl;
    read(root);    
    cout<<endl;
    root = delete_node(root, 100);
    read(root);
    cout<<endl;

}