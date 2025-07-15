#include<iostream>
#include<queue>
#include<vector>
#include<unordered_map>
using namespace std;
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for(int i=0; i<nums.size(); i++){
            freq[nums[i]] += 1; 
        }

        priority_queue<pair<int, int>> q;
        for(auto [k, v]: freq){
            q.push({v, k});
        }
        nums.clear();
        int n = q.size();
        for(int i=0; i<k; i++){
            nums.push_back(q.top().second);
            q.pop();
        }
        return nums;
    }
};

int main() {
    Solution soln;
    vector<int> nums = {1, 1, 1, 2, 2, 3};
    int k = 2;
    vector<int> result = soln.topKFrequent(nums, k);
     
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}