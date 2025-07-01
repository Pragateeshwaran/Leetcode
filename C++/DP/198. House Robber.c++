#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 0);

        dp[0] = 0;
        dp[1] = nums[0];

        for(int i=2; i<n+1; i++){
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1]);
        }
        for(int i=0; i<n+1; i++){
            std::cout << dp[i] << " ";
        }
        return dp[n];
    }
};

int main(){
    Solution* soln = new Solution();
    vector<int> nums = {2,7,9,3,1};
    int res = soln->rob(nums);
    cout << res <<endl;
}