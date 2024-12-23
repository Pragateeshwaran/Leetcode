#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans = {{1}};
        
        for (int rowNum = 2; rowNum <= numRows; ++rowNum) {
            vector<int> row;
            const vector<int>& prevRow = ans.back();
            
            // Compute the current row
            for (int i = 0; i < prevRow.size() - 1; ++i) {
                row.push_back(prevRow[i] + prevRow[i + 1]);
            }
            row.insert(row.begin(), 1); // Add 1 at the start
            row.push_back(1);          // Add 1 at the end
            
            ans.push_back(row);
        }
        
        return ans;
    }
};

int main() {
    Solution solution;
    int numRows = 5;
    vector<vector<int>> result = solution.generate(numRows);
    
    for (const auto& row : result) {
        for (int num : row) {
            cout << num << " ";
        }
        cout << endl;
    }

    return 0;
}
