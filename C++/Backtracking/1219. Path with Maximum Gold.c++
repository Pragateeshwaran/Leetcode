#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    vector<int> result;
    vector<pair<int, int>> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    int getMaxGold(int i, int j, vector<vector<int>>& grid, vector<vector<bool>>& visited, int m, int n){
        if(i < 0 || j < 0 || i >= m || j >= n){
            return  0;
        }
        if(visited[i][j] == true || grid[i][j] == 0)
            return 0;
        int sums = grid[i][j];
        int bestPathSum = 0;
        visited[i][j] = true;
        for(pair<int, int> direct: directions){
            int x = direct.first;
            int y = direct.second;
            int pathSum = getMaxGold(i+x, j+y, grid, visited, m, n);
            result.push_back(sums);
            if(pathSum > bestPathSum)
                bestPathSum = pathSum ;
        }
        visited[i][j] = false;
        return sums + bestPathSum;

    }
    int getMaximumGold(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int ans = 0;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                vector<vector<bool>>visited (m, vector<bool>(n, false)); 
                int current = getMaxGold(i, j, grid, visited, m, n);
                result.push_back(current);
                if (current > ans) ans = current;
            }
        }
               
        return ans;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> grid = {
        {0, 6, 0},
        {5, 8, 7},
        {0, 9, 0}
    };
    
    cout << sol.getMaximumGold(grid) << endl;  
    return 0;
}