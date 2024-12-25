#include<iostream>
#include<vector>
using namespace std;

class Solution{
    public:
        vector<int> getRow(int rowIndex){
            vector<vector<int>> result = {{1}};
            
            for(int i=1; i <= rowIndex; i++){
                vector<int> row;
                row.push_back(1);
                for(int j=1; j < result[i-1].size()-1; j++){
                    row.push_back(result[i-1][j-1] + result[i-1][j]);
                }
                row.push_back(1);
                result.push_back(row);
            }
            return result[rowIndex];
        }
};
int main(){
    Solution solution;
    int rowIndex = 3;
    vector<int> result = solution.getRow(rowIndex);
    for(int num : result){
        cout << num << " ";
    }
    cout << endl;
    return 0;
}