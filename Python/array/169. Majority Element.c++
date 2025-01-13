// Given an array nums of size n, return the majority element.

// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

// Example 1:

// Input: nums = [3,2,3]
// Output: 3

// Example 2:

// Input: nums = [2,2,1,1,1,2,2]
// Output: 2

#include <iostream>
#include <vector>
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
    vector<int> nums = {3, 2, 3};
    Solution sol;
    cout << sol.majorityElement(nums) << endl;
    return 0;
}