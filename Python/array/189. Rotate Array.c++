// Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

// Example 1:

// Input: nums = [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]

// Example 2:

// Input: nums = [-1,-100,3,99], k = 2
// Output: [3,99,-1,-100]
// Explanation: 
// rotate 1 steps to the right: [99,-1,-100,3]
// rotate 2 steps to the right: [3,99,-1,-100]

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n; 

        for (int i = 0; i < k; i++) {
            int temp = nums[n - 1];  
 
            for (int j = n - 1; j > 0; j--) {
                nums[j] = nums[j - 1];
            }

            nums[0] = temp;  
        }
    }
};

// class Solution {
// public:
//     void rotate(vector<int>& nums, int k) {
//         int n = nums.size();
//         k = k % n; // Handle cases where k > n

//         // Reverse the whole array
//         reverse(nums.begin(), nums.end());
//         // Reverse the first k elements
//         reverse(nums.begin(), nums.begin() + k);
//         // Reverse the remaining elements
//         reverse(nums.begin() + k, nums.end());
//     }
// };

int main() {
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    int k = 3;

    Solution s;
    s.rotate(nums, k);

    for (int i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }

    return 0;
}