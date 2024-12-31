#include <iostream>
#include<unordered_map>
#include <vector>
#include <algorithm> // For std::min
using namespace std;
class Solution {
public:
    vector<int> costs, days;
    unordered_map<int, int> dict;
    int dfs(int i){
        if(i >= days.size())
            return 0;
        if(dict.find(i)!=dict.end())
            return dict[i];
        
        int j = i;
        while (j < days.size() and days[j] <= days[i] + 6)
            j++;
        
        int k = i;
        while (k < days.size() and days[k] <= days[i] + 29)
            k++;
        
        int sums = min(
            (dfs(i+1) + costs[0]), 
            min(
                (dfs(j) + costs[1]),
                (dfs(k) + costs[2])
            )
        );

        dict[i] = sums;

        return sums;      

    }
    int mincostTickets(vector<int>& day, vector<int>& cost) {
        days = day;
        costs = cost;
        return dfs(0);
    }
};




// class Solution {
// public:
//     int mincostTickets(vector<int>& days, vector<int>& costs) {
//         vector<int> dp(366, 0); // DP array for up to day 365
//         int n = days.size();
//         int j = 0; // Pointer for the travel days array
        
//         for (int i = 1; i <= 365; i++) {
//             if (j >= n) {
//                 break; // All travel days processed
//             }
//             if (i != days[j]) {
//                 dp[i] = dp[i - 1]; // If it's not a travel day, cost stays the same
//             } else {
//                 // Calculate the minimum cost for this travel day
//                 dp[i] = min(
//                     dp[i - 1] + costs[0], 
//                     min(dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
//                 );
//                 j++; // Move to the next travel day
//             }
//         }
//         return dp[days[n - 1]]; // Return the cost for the last travel day
//     }
// };

int main() {
    Solution solution;
    vector<int> days = {1, 4, 6, 7, 8, 20};
    vector<int> costs = {2, 7, 15};
    cout << solution.mincostTickets(days, costs) << endl; // Output: 11
    return 0;
}
