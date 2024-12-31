#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0, min_purchase = prices[0];
        for(int i=1; i<prices.size(); i++){
            max_profit = max(max_profit, prices[i] - min_purchase);
            min_purchase = min(min_purchase, prices[i]);
        }
        return max_profit;
    }
};

int main(){
    Solution s;
    vector<int> prices = {7,1,5,3,6,4};
    cout << s.maxProfit(prices);
}