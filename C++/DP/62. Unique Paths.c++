#include <vector>
#include<iostream>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        // Create m x n grid initialized with 0
        vector<vector<int>> Result(m, vector<int>(n, 0));  
        
        // Set destination cell to 1
        Result[m-1][n-1] = 1;  
        
        // Traverse from bottom-right to top-left
        for(int row = m-1; row >= 0; row--) {
            for(int col = n-1; col >= 0; col--) {
                // Skip the destination cell since it's already set
                if(row == m-1 && col == n-1) 
                    continue;
                    
                // Calculate paths by adding paths from right and bottom cells
                int rightPaths = (col + 1 < n) ? Result[row][col+1] : 0;
                int downPaths = (row + 1 < m) ? Result[row+1][col] : 0;
                Result[row][col] = rightPaths + downPaths;
            }
        }
        
        return Result[0][0];
    }
};

// Test the solution
int main() {
    Solution solution;
    
    // Test cases
    cout << "Paths for 3x3 grid: " << solution.uniquePaths(3, 3) << endl;  // Should output 6
    cout << "Paths for 3x7 grid: " << solution.uniquePaths(3, 7) << endl;  // Should output 28
    cout << "Paths for 7x3 grid: " << solution.uniquePaths(7, 3) << endl;  // Should output 28
    cout << "Paths for 3x2 grid: " << solution.uniquePaths(3, 2) << endl;  // Should output 3
    
    return 0;
}
