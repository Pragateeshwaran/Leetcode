#include <vector>
#include <iostream>

using namespace std;

class Solution {
private:
    void helper(vector<int>& nums, vector<bool>& used, vector<int>& sub, vector<vector<int>>& res) {
        if (sub.size() == nums.size()) {
            res.push_back(sub);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (!used[i]) {  
                used[i] = true;
                sub.push_back(nums[i]);
                helper(nums, used, sub, res);
                sub.pop_back();
                used[i] = false;
            }
        }
    }

public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<bool> used(nums.size(), false);
        vector<int> sub;
        vector<vector<int>> res;
        helper(nums, used, sub, res);
        return res;
    }
};

int main() {
    vector<int> nums = {1, 2, 3};
    Solution obj;

    vector<vector<int>> res = obj.permute(nums);

    cout << "Permutations:\n";
    for (const auto& perm : res) {
        cout << "[ ";
        for (int num : perm) {
            cout << num << " ";
        }
        cout << "]\n";
    }

    return 0;
}
