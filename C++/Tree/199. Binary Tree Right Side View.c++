#include<iostream>
#include<queue>
#include<vector>
using namespace std;

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
    vector<int> rightSideView(TreeNode* root) {
        if(not root)
            return {};
        queue<TreeNode*> q;
        vector<int> result;
        q.push(root);
        while(!q.empty()){
            vector<TreeNode*> level;
            TreeNode* Node;
            int n = q.size();
            for(int i=0; i<n; i++){
                Node = q.front();
                q.pop();
                if(Node->left)
                    q.push(Node->left);
                if(Node->right)
                    q.push(Node->right);

            }
            result.push_back(Node->val);
        }
        return result;
    }
};

void inorderTraversal(TreeNode* root) {
    if (!root) return;
    
    inorderTraversal(root->left);
    cout << root->val << " ";
    inorderTraversal(root->right);
}

int main(){
    Solution sol;
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->right = new TreeNode(3);
    root->right->right->right = new TreeNode(4);
    root->left = new TreeNode(5);

    vector<int> result = sol.rightSideView(root);
    inorderTraversal(root);
    for(int val : result) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}