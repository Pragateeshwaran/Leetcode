#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int res, votes = 0;
        for(int i=0; i<nums.size(); i++){
            if(votes == 0)
                res = nums[i];
            if (nums[i] == res)
                votes += 1;
            else
                votes -= 1;
        }
        return res;
    }
};
int main() {
    Solution s;
    vector<int> nums = {2,2,1,1,1,2,2};
    cout << s.majorityElement(nums);
}
