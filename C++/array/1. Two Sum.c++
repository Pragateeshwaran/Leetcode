#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;
class Solution{
    public:
        vector<int> twoSum(vector<int> &nums, int target){
            unordered_map<int, int> dictionary;
            for(int i = 0; i < nums.size(); i++){
                // x + y = t  => y = t - x
                int y = target - nums[i];
                if(dictionary.find(y) != dictionary.end()){
                    return {dictionary[y], i};
                }
                dictionary[nums[i]] = i;
            }
            return {};
        }
};
int main(){
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    Solution soln;
    vector<int> res = soln.twosum(nums, target);
    cout << res[0] << "\t" <<res[1] << endl;
    return 0;
}