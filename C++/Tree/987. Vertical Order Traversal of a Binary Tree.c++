#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>
#include<utility>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
    map<int, vector<pair<int, int>>> columnTable;

    vector<vector<int>> verticalTraversal(TreeNode* root) {
        if (!root) return {};
 
        queue<pair<TreeNode*, pair<int, int>>> q;
        q.push({root, {0, 0}});   

        while (!q.empty()) {
            auto [node, pos] = q.front();
            q.pop();
            int x = pos.first;
            int y = pos.second;

            columnTable[x].push_back({y, node->val});

            if (node->left) q.push({node->left, {x - 1, y + 1}});
            if (node->right) q.push({node->right, {x + 1, y + 1}});
        }

        vector<vector<int>> ans;
        for (auto& [x, vec] : columnTable) {
            // Sort first by row (y), then by val
            sort(vec.begin(), vec.end(), [](pair<int, int>& a, pair<int, int>& b) {
                if (a.first == b.first)
                    return a.second < b.second;
                return a.first < b.first;
            });

            vector<int> col;
            for (auto& [y, val] : vec) {
                col.push_back(val);
            }
            ans.push_back(col);
        }

        return ans;
    }
};


// class Solution {
// public:
//     map<int, vector<int>> maps;
//     vector<vector<int>> verticalTraversal(TreeNode* root) {
//         if(!root)
//             return {{}};
//         queue<pair<TreeNode*, int>> q;
//         q.push({root, 0});
//         while(!q.empty()){
//             TreeNode* Node = q.front().first;
//             int idx = q.front().second;
//             q.pop();
//             maps[idx].push_back(Node->val);
//             if(Node->right)
//                 q.push({Node->right, idx+1});
//             if(Node->left)
//                 q.push({Node->left, idx-1});
//         }

//         for(int i = 0; i < maps.size(); i++){
//             sort(maps[i].begin(), maps[i].end());
//         }

//         vector<vector<int>> ans;
//         for(auto it : maps){
//             ans.push_back(it.second);
//         }
//         return ans;
//     }
// };

int main(){
    // Example usage
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left = new TreeNode(15);
    root->right->right = new TreeNode(7);

    Solution sol;
    vector<vector<int>> result = sol.verticalTraversal(root);

    for(const auto& vec : result) {
        for(int val : vec) {
            cout << val << " ";
        }
        cout << endl;
    }

    return 0;
}