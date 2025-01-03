#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        int n = nums.size();  // Use `size()` for vector
        long long sumTotal = 0;  // Use `long long` for large sums
        long long sumCurr = 0; 
        int cnt = 0;

        // Calculate total sum
        for (int i = 0; i < n; i++) {
            sumTotal += nums[i];
        }

        // Check valid splits condition
        for (int i = 0; i < n - 1; i++) {  // `n - 1` to ensure at least one element in the right subarray
            sumCurr += nums[i];
            if (sumCurr >= sumTotal - sumCurr) {  // Valid split condition
                cnt++;
            }
        }

        return cnt;
    }
};
int main(){
    Solution solution;
    vector<int> nums = {1, 2, 2, 2, 5, 0};
    cout << (solution.waysToSplitArray(nums) == 3);
    return 0;
}