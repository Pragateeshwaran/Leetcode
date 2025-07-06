#include<iostream>
#include<vector>
using namespace std;
// class Solution {
// public:
//     int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
//         int maxi = -1;
//         int n = customers.size();
//         for(int i=0; i<n; i++){
//             int lenght = 0;
//             int m = minutes;
//             int j = 0;
//             int sums = 0;
//             while(j<n){
//                 if(grumpy[j] == 1 and  (j >= i and j < i+minutes)){
//                     sums += customers[j];
//                 }
//                 else if(grumpy[j] == 0){
//                     sums += customers[j];
//                 }
//                 j++;
                
//             }
//             cout<<sums<<endl;
//             maxi = max(maxi, sums); 
            
//         }
//         return maxi;
//     }
// };

class Solution {
public:
    int maxSatisfied(vector<int>& customers, vector<int>& grumpy, int minutes) {
        int initialSatisfaction = 0;
        int maxExtraSatisfaction = 0;
        int currentWindowSatisfaction = 0;
        
        for (int i = 0; i < customers.size(); ++i) {
            if (grumpy[i] == 0) {
                initialSatisfaction += customers[i];
            } else if (i < minutes) {
                currentWindowSatisfaction += customers[i];
            }
        }
        
        maxExtraSatisfaction = currentWindowSatisfaction;
        
        for (int i = minutes; i < customers.size(); ++i) {
            currentWindowSatisfaction += customers[i] * grumpy[i];
            currentWindowSatisfaction -= customers[i - minutes] * grumpy[i - minutes];
            maxExtraSatisfaction = max(maxExtraSatisfaction, currentWindowSatisfaction);
        }
        
        return initialSatisfaction + maxExtraSatisfaction;   
    }
};

int main(){
    Solution* soln = new Solution();
    cout << "Test Case 1: " << endl;
    vector<int> customers1 = {1,0,1,2,1,1,7,5};
    vector<int> grumpy1 = {0,1,0,1,0,1,0,1,0};
    int minutes1 = 3;
    int res1 = soln->maxSatisfied(customers1, grumpy1, minutes1);
    cout << "Expected: 16, Got: " << res1 << endl;
    cout << "Test Case 2: " << endl;
    vector<int> customers3 = {1,0,1,2,1,1,7,5};
    vector<int> grumpy3 = {0,1,0,1,0,1,0,1,0};
    int minutes3 = 5;
    int res3 = soln->maxSatisfied(customers3, grumpy3, minutes3);
    cout << "Expected: 18, Got: " << res3 << endl;
}