#include<iostream>
#include<vector>
using namespace std;    

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int idx = 0;
        for(int i=0; i<nums.size(); i++){
            if(nums[i] != val){
                nums[idx] = nums[i];
                idx++;
            }
        }
        return idx;
    }
};

int main(){
    Solution solution;
    vector<int> nums = {3, 2, 2, 3};
    int val = 3;
    cout << "Length of new array: " << solution.removeElement(nums, val) << endl;
    return 0;
}