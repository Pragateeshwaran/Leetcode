#include<vector>
#include<iostream>
using namespace std;
class Solution {
private:
    vector<vector<int>>combinationSumHelp(vector<int>& candidates, int target, vector<vector<int>>& res, vector<int>& sub, int index){
        if(target == 0){
            res.push_back(sub);
            return res;
        }
        for(int i = index; i< candidates.size(); i++){
            sub.push_back(candidates[i]);
            if(target - candidates[i] < 0){
                sub.pop_back();
                continue;
            }
            combinationSumHelp(candidates, target - candidates[i], res, sub, i);
            sub.pop_back();
        }
        return res;
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target){
        vector<vector<int>> res;
        vector<int> sub;
        return combinationSumHelp(candidates, target, res, sub, 0);
    }
};

int main(){
    vector<int> candidates = {2,3,6,7};
    int target = 7;
    Solution obj;
    vector<vector<int>> res = obj.combinationSum(candidates, target);
    for(int i = 0; i < res.size(); i++){
        for(int j = 0; j < res[i].size(); j++){
            cout << res[i][j] << " ";
        }
        cout << endl;
    }
    return 0; 
}