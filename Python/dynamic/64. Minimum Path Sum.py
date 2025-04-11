# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

 

# Example 1:

# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12


from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dfs(i, j): 
            if i >= m or j >= n:
                return float("inf") 
            if i == m - 1 and j == n - 1:
                return grid[i][j] 
            if (i, j) in memo:
                return memo[(i, j)]
 
            down = dfs(i + 1, j)
            right = dfs(i, j + 1)
            memo[(i, j)] = grid[i][j] + min(down, right)

            return memo[(i, j)]

        return dfs(0, 0)

soln = Solution()
print(soln.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Output: 7 

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Initialize a DP table with the same dimensions as the grid
        dp = [[0] * n for _ in range(m)]
        
        # Fill the DP table
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:  # Starting point
                    dp[i][j] = grid[i][j]
                elif i == 0:  # First row (can only come from the left)
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:  # First column (can only come from above)
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:  # General case
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        
        # The result is in the bottom-right corner of the DP table
        return dp[m - 1][n - 1]

soln = Solution()
print(soln.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # Output: 7 