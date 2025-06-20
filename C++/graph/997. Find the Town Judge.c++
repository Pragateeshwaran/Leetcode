#include<iostream>
#include<vector>
using namespace std;
// class Solution {
// public:
//     int findJudge(int n, vector<vector<int>>& trust) {
//         unordered_map<int, vector<int>> trust_dictionary;
//         for(int i = 1; i <= n; i++){
//             trust_dictionary[i] = {};
//         }
//         for(int i = 0; i < trust.size(); i++){
//             trust_dictionary[trust[i][0]].push_back(trust[i][1]);
//         }
        
//         int judge = -1;
//         for(int i=1; i<=n; i++){
//             if(trust_dictionary[i].empty()){
//                 judge = i;
//             }
//         }

//         int res = judge;
//         // cout<<res;
//         for(int i = 1; i<=n; i++){
//             vector<int> new_vec(trust_dictionary[i].begin(), trust_dictionary[i].end());
//             if(i!=judge){
//                 auto it = find(new_vec.begin(), new_vec.end(), judge);
//                 if(it == new_vec.end()){
//                     res = -1;
//                 }
//             }
//         }
//         return res;   
//     }
// };

class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        if(trust.size()==0 && n==1) return 1;
        if(trust.size()==0 && n>1) return -1;

        vector<int> trusted(n+1,0);
        vector<int> trusts(n+1,0);
        
        for(int i=0;i<trust.size();i++){
            int a=trust[i][1];
            int b=trust[i][0];

            trusted[a]++;
            trusts[b]++;
        }

        for(int i=0;i<n+1;i++){
            if(trusted[i]==n-1 && trusts[i]==0) return i;
        }
        
        return -1;
    }
};

int main() {
    Solution solution;
    vector<vector<int>> trust = {{1, 2}, {2, 3}, {3, 1}};
    int n = 3;
    cout << solution.findJudge(n, trust) << endl; // Output: -1
    return 0;
}