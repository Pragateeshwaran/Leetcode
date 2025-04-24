#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

// struct TreeNode {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
// };

class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) return res;  
        
        queue<TreeNode*> Q;
        Q.push(root);

        while (!Q.empty()) {
            vector<int> sub;
            int size = Q.size();  

            for (int i = 0; i < size; i++) {
                TreeNode* curr = Q.front();
                Q.pop();
                sub.push_back(curr->val);

                if (curr->left) Q.push(curr->left);
                if (curr->right) Q.push(curr->right);
            }
            res.push_back(sub);
        }

         
        return reverse(res.begin(), res.end());;
    }
};
